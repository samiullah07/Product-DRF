from rest_framework import serializers
from .models import Product, ProductGenric

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['url',"name","description","price"]

    def validate_name(self, value):
        qs = Product.objects.filter(name__iexact = value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already exist")
        
        return value



class ProductGenericSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductGenric
        fields = ["name","category"]

