from django import forms
from .models import Product  # Import the Product model


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'make', 'model', 'asset_tag', 'serial_number', 'note']
