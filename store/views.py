import google.generativeai as genai
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.conf import settings
from pymongo import MongoClient
import requests

genai.configure(api_key=settings.GEMINI_API_KEY)
client = MongoClient(settings.MONGO_URI)
db = client["ecommerce_db"]
collection = db["tags"]

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

def add_product(request):
    suggested_tags = []
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product_name = form.cleaned_data['name']
            product_description = form.cleaned_data['description']

            prompt = f"Suggest 5 short, relevant tags for a product named '{product_name}' with description '{product_description}'. List them comma-separated."

            try:
                model_name = 'models/gemma-3-12b-it'
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(prompt)
                tags_text = response.text
                suggested_tags = [tag.strip() for tag in tags_text.replace('\n', ',').split(',') if tag.strip()]
                print("Gemini Suggested tags:", suggested_tags)

                # Get manually entered tags from the form
                manual_tags = form.cleaned_data.get('tags')
                final_tags = []
                if manual_tags:
                    final_tags.extend([tag.strip() for tag in manual_tags.split(',')])
                final_tags.extend(suggested_tags)
                product.tags = list(set(final_tags)) # Ensure unique tags

                print("Final tags to save to Product:", product.tags)
                product.save()

                if suggested_tags:
                    tag_data = {
                        "product_id": str(product._id),
                        "tags": suggested_tags
                    }
                    collection.insert_one(tag_data)
                    print("Suggested tags saved to MongoDB")

                return redirect('product_list')
            except Exception as e:
                print("Gemini API Error:", e)
                return render(request, 'store/add_product.html', {'form': form, 'suggested_tags': [], 'error': f'Gemini API error: {str(e)}'})
        else:
            print("Form errors:", form.errors)
            return render(request, 'store/add_product.html', {'form': form, 'suggested_tags': []})
    else:
        form = ProductForm()
    return render(request, 'store/add_product.html', {'form': form, 'suggested_tags': []})