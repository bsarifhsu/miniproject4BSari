# INF601 - Advanced Programming in Python
# Bunyamin Sari
# Mini Project 4

from django.contrib import admin

from .models import Product, CheckOut, CheckIn


class ProductAdmin(admin.ModelAdmin):
    list_display = ["asset_tag", "name", "make", "model", "serial_number", "checked_out_by_name"]
    list_filter = ["make", "name"]

    def checked_out_by_name(self, obj):
        # Check if there is a related CheckOut object for the product
        checkout = CheckOut.objects.filter(product=obj).first()

        if checkout:
            # Access the User object related to the CheckOut instance
            checkout_user = checkout.checked_out_by
            if checkout_user:
                # Display the username of the User
                return checkout_user.username

        return "Not checked out yet!"  # You can customize this to display any text for products not checked out

    checked_out_by_name.short_description = "Checked Out By"  # Custom column header


admin.site.register(Product, ProductAdmin)
admin.site.register(CheckOut)
admin.site.register(CheckIn)
