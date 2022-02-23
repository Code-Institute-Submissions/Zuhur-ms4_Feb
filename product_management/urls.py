from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_management, name='product-management'),
    path('add_product/', views.add_product, name='add-product'),
]