from django import forms
from merchandise.models import Merchandise


class ProductForm(forms.ModelForm):
    class Meta:
        model = Merchandise
        fields = '__all__'
