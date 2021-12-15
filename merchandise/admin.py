from django.contrib import admin
from .models import Merchandise, Category

# Register your models here.
admin.site.register(Merchandise)
admin.site.register(Category)