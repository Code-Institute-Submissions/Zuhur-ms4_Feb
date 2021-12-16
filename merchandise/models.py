from django.db import models

# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.friendly_name


class Merchandise(models.Model):

    class Meta:
        verbose_name_plural = 'Merchandise'


    name = models.CharField(max_length=250)
    description = models.TextField()
    sku = models.CharField(max_length=250, null=True, blank=True)
    category =  models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
