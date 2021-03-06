from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_management, name='product-management'),
    path('add_product/', views.add_product, name='add-product'),
    path('edit_product/<str:pk>/', views.edit_product, name='edit-product'),
    path('delete_product/<str:pk>/', views.delete_product, name='delete-product'),
]