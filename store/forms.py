from django import forms
from django.forms import ModelForm
from .models import Product


# Create a product form
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'created_by',
         'title', 'description', 'price', 'in_stock', 'is_active',)    
         #what fields to add in the product
         