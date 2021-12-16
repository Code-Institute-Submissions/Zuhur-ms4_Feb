from django.contrib import admin
from .models import Merchandise, Category

# Register your models here.

class MerchandiseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Merchandise, MerchandiseAdmin)
admin.site.register(Category, CategoryAdmin)