from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.conf import settings
import openai

# Set your OpenAI API key
openai.api_key = settings.OPENAI_KEY

# Auto-tag generation logic
def generate_tags(description):
    prompt = f"Suggest 5 relevant and short tags for this product description: \"{description}\""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates short product tags."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=50,
        )
        tags_text = response['choices'][0]['message']['content']
        tags = [tag.strip().strip('#') for tag in tags_text.split(",")]
        return tags
    except Exception as e:
        print("OpenAI error:", e)
        return []

# Show all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

# Add product with auto-tags
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.tags = generate_tags(product.description)
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'store/add_product.html', {'form': form})
