# INF601 - Advanced Programming in Python
# Bunyamin Sari
# Mini Project 4

from django import forms
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'make', 'model', 'asset_tag', 'serial_number', 'note']


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')  # You can include additional fields as needed
