from rest_framework import serializers
from .models import Product, ProductGenric

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name","description","price"]



class ProductGenericSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductGenric
        fields = ["name","category"]

