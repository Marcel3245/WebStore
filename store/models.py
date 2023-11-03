from django.db import models
from django.urls import reverse
from django.conf import settings

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


#Category of products, table SQL
class Category(models.Model):
    name                    = models.CharField(max_length=255, db_index=True)
    slug                    = models.SlugField(max_length=255, unique=True)  # http://127.0.0.1:8000/...(slug).../

    #More instruction about a category table
    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name
#Data about a product (')
class Product(models.Model):
    category                = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by              = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='product_creator', on_delete=models.CASCADE, blank=True)
    title                   = models.CharField(max_length=255, blank=True)
    author                  = models.CharField(max_length=255, default='admin')
    description             = models.TextField(max_length=300, blank=True)
    specification           = models.TextField(blank=True)
    image                   = models.ImageField(upload_to='images/', default='images/default.jpg', blank=True) #Every product only one image!!
    slug                    = models.SlugField(max_length=255, blank=True)
    price                   = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock                = models.BooleanField(default=True)
    is_active               = models.BooleanField(default=True)
    created                 = models.DateTimeField(auto_now_add=True) #It will happend only once!!
    updated                 = models.DateTimeField(auto_now=True) #Every time after update!!
    objects                 = models.Manager()
    products                = ProductManager()

    #Products ordering
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created', ) #(-)Descending order

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    #What do we want to get in the end
    def __str__(self):
        return self.title