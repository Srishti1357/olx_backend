from rest_framework import serializers
from .models import Category, Product, Cart,  Favorite
from django.contrib.auth.models import User



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'available','image']


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'product']

class CartSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True, read_only=True)  # Nested serializer for products

    class Meta:
        model = Cart
        fields = ['id', 'user', 'products']  # Include user and products in the serialized data
        read_only_fields = ['user']  # User should not be set directly