from django.test import TestCase
from .models import Category, Merchandise, Gender


class TestModel(TestCase):
    

    def test_string(self):
        merch = Merchandise.objects.create(name="head band", price=3.99, description="tennis head band")

        self.assertEqual(str(merch), merch.name)

    