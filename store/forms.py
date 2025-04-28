from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    tags = forms.CharField(max_length=200, required=False, help_text="Enter tags separated by commas")

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'tags']