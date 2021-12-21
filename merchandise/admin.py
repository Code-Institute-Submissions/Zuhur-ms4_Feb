from django.contrib import admin
from .models import Merchandise, Category, Gender


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
admin.site.register(Gender)
