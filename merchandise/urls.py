from django.urls import path
from . import views

urlpatterns = [
    path('', views.merchandise, name='merch'),
    path('<merch_id>', views.merchandise_detail, name='merch-detail')
]

