from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view-bag'),
    path('add/<item_id>', views.add_to_cart, name='add-to-cart'),
    path('edit/<item_id>', views.edit_cart, name='edit-cart'),
    path('delete/<item_id>', views.delete_item, name='delete-cart'),
]