from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

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
