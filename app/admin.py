from django.contrib import admin
from .models import Product, Favorite, Category, Cart

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favorite)
admin.site.register(Category)
