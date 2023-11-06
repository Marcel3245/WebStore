from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_all, name='product_all'),
    path('about/', views.about, name='about'),
    path('item/<slug:slug>/', views.product_detail, name="product_detail"),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
    path('delete_event/<slug:slug>/', views.delete_event, name='delete_event'),
    path('store/admin_view/', views.admin_view, name='admin_view'),
    path('store/amdin/add_product', views.add_product, name="add-product"),
    path('list_product', views.list_product, name="list-product"),
    path('search/', views.product_search, name='product_search'),
]