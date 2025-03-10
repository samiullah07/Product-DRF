from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, ProductGenric
from .serializers import ProductSerializers, ProductGenericSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets,generics
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





class ProductGenricViewSet(generics.RetrieveAPIView):
    queryset = ProductGenric.objects.all()
    serializer_class = ProductGenericSerializers


product_generic = ProductGenricViewSet.as_view()




class ProductGenricListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


product_List_generic = ProductGenricListView.as_view()





    
    
