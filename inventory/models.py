from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=50, default="Make")
    model = models.CharField(max_length=50, default="Model")
    asset_tag = models.CharField(max_length=20, default="N/A", unique=True)
    serial_number = models.CharField(max_length=50, default="Serial Number", unique=True)
    note = models.TextField(default="No notes available")

    def __str__(self):
        return self.name


class CheckOut(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    checked_out_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    checked_out_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - Checked Out by {self.checked_out_by.username} on {self.checked_out_date}"


class CheckIn(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    checked_in_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    checked_in_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - Checked In by {self.checked_in_by.username} on {self.checked_in_date}"
