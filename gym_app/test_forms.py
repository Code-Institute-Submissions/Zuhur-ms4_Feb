from django.test import TestCase
from .forms import ContactForm
# Create your tests here.

class TestContactForm(TestCase):
    # Test to see if shopping bag template is rendered
    def test_email_field(self):
        form = ContactForm ({
            'first_name': 'james',
            'last_name': 'jamerson',
            'email': 'jamesgmail.com',
            'message': 'hello this is a message'
        })
        self.assertFalse(form.is_valid())
    

    def test_all_fields_required(self):
         form = ContactForm ({
             'first_name': '',
             'last_name': '',
             'email': 'jamesgmail.com',
             'message': 'hello this is a message',
         })
         self.assertFalse(form.is_valid())
