from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =           ['name', 'slug']                     #Create a connection between slug and name(they are the same)
    prepopulated_fields =    {'slug':('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =          ['title', 'author', 'slug', 'price',
                            'in_stock', 'created', 'updated']     #Filtering a products by
    list_filter =           ['in_stock', 'is_active']
    list_editable =         ['price', 'in_stock']                 #Data posible to edit
    prepopulated_fields =   {'slug':('title',)} 