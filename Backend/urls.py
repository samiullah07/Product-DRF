from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'v1', ProductViewSet)

urlpatterns = [
    path('',views.api,name="name"),
    path('', include(router.urls)),
]