from django.test import TestCase

# Create your tests here.

class TestViews(TestCase):
    # Test to see if shopping bag template is rendered
     def test_get_home_page(self):
         response = self.client.get('/')
         self.assertEqual(response.status_code, 200)
         self.assertTemplateUsed(response, 'gym_app/home.html')
