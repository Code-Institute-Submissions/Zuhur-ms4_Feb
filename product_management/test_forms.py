from django.test import TestCase
from .forms import ProductForm
# Create your tests here.

class TestContactForm(TestCase):
    # Test to see if shopping bag template is rendered
    def test_add_product_with_unrequired_fields(self):
        form = ProductForm ({
            'name': 'Socks',
            'description': 'Must add',
            'sku': '',
            'category': '',
            'gender': '',
            'price': 9.99,
            'image_url': '',
            'image': '',
        })
        self.assertTrue(form.is_valid())
    
    def test_add_product_without_required_fields(self):
        form = ProductForm ({
            'name': '',
            'description': 'Must add',
            'sku': '',
            'category': '',
            'gender': 'Men',
            'price': 9.99,
            'image_url': '',
            'image': '',
        })
        self.assertFalse(form.is_valid())
