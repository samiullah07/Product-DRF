from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,product_generic,product_List_generic

router = DefaultRouter()
router.register(r'v1', ProductViewSet),
# router.register(r'generics', product_generic,basename="product_Generic")


urlpatterns = [
    path('',views.api,name="name"),
    path('', include(router.urls)),
    path('generics/<int:pk>',product_generic,name="Product-Generic"),
    path("generic-list/",product_List_generic,name="Product-List")
]