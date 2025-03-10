from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from .serializers import ProductSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
# Create your views here.

@api_view(['GET'])
def api(request):
    product = Product.objects.all().order_by("?").first()
    data = {}

    if product:
        data = ProductSerializers(product).data

    return Response(data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    
    
