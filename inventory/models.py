# INF601 - Advanced Programming in Python
# Bunyamin Sari
# Mini Project 4


from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=50, default=" ")
    model = models.CharField(max_length=50, default=" ")
    asset_tag = models.CharField(max_length=20, default=" ", unique=True)
    serial_number = models.CharField(max_length=50, default=" ", unique=True)
    note = models.TextField(default=" ")
    is_checked_out = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def save(self, *args, **kwargs):
        if not self.created_by_id:
            # Set the default value to the currently logged-in user when the product is created
            self.created_by = User.objects.get(
                username='Admin')  # Replace 'default_user' with an appropriate default username
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class CheckOut(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Adjust this according to your model structure
    checked_out_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='checked_out_products')  # Specify related_name
    checked_out_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.product.name} - Checked Out by {self.checked_out_by.username} on {self.checked_out_date}"


class CheckIn(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    checked_in_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    checked_in_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - Checked In by {self.checked_in_by.username} on {self.checked_in_date}"



