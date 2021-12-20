import decimal
import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from decimal import Decimal

from merchandise.models import Merchandise

# Create your models here.

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    address_line_1 = models.CharField(max_length=95, null=False, blank=False)
    address_line_2 = models.CharField(max_length=95, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True) # not required
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _str__(self):
        return self.order_number

    def _order_number(self):
        return uuid.uuid4().hex.upper()
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._order_number()
        super().save(*args, **kwargs)
    
    def update_total(self):
        self.delivery_cost = decimal.Decimal(4.99)
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()
    


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    merch = models.ForeignKey(Merchandise, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def _str__(self):
        return self.order_number

    def save(self, *args, **kwargs):
        self.lineitem_total = self.merch.price * self.quantity
        super().save(self, *args, **kwargs)
