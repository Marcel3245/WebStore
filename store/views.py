from django.shortcuts import get_object_or_404, render, redirect
from .models import Category, Product

#Wiliam's
from django.http import HttpResponseRedirect 
from .forms import ProductForm

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

def delete_event(request, slug):
    product = get_object_or_404(Product, slug=slug)
    product.delete()
    return redirect('store:product_all')

def admin_view(request):
    return render(request, 'store/admin_view.html')

def product_search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched_product = Product.objects.filter(title=searched) 
        return render(request, 'store/search_product.html', {'searched':searched, 'searched_product':searched_product})
    else:
        return render(request, 'store/search_product.html', {})


#Wiliam's
#adding and saving new product
def add_product(request):
    submitted = False
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_poduct?submitted=true')
    else: 
        form = ProductForm
        if 'submitted' in request.GET:
            submitted = True 

    return render(request, 'store/add_product.html',{'form':form, 'submitted':submitted})
def all_store(request):
    store_list = Product.objects.all
    return render(request, 'store/store_list.html', {'store_list': store_list})
def list_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    product_list = Product.objects.all
    return render(request, 'store/product.html', {'product_list': product_list}) 

