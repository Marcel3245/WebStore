from django.shortcuts import get_object_or_404, render
from .models import Category, Product


#User request inforamtion
def product_all(request):
    #Query from sql, products in database 
    products = Product.objects.all()
    #Load a associated template
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    specifications = product.specification.split('\n')
    availability = "Available" if product.in_stock else "Not available"
    return render(request, 'store/detail.html', {'product':product, 'specifications': specifications, 'availability': availability})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category.html', {'category':category, 'products':products})

def about(request):
    return render(request, 'store/about.html')
