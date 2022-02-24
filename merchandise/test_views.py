from django.test import TestCase
from .models import Merchandise
# Create your tests here.

class TestViews(TestCase):
    # Test to see if shopping bag template is rendered
    def test_get_merch(self):
        response = self.client.get('/merch/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'merchandise/merch.html')
    

    def test_get_merch_detail(self):
        merch = Merchandise.objects.create(name='trousers', price=9.99)
        response = self.client.get(f'/merch/{merch.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'merchandise/merch_detail.html')