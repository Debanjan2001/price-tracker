from rest_framework import serializers
from .models import Product, PriceData

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'url', 'website']

class PriceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceData
        fields = ['id', 'price', 'timestamp']