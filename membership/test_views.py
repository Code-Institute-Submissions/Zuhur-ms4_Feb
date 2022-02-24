from django.test import TestCase

# Create your tests here.

class TestViews(TestCase):
    # Test to see if shopping bag template is rendered
     def test_get_membership_page(self):
         response = self.client.get('/membership/')
         self.assertEqual(response.status_code, 200)
         self.assertTemplateUsed(response, 'membership/membership.html')