# INF601 - Advanced Programming in Python
# Bunyamin Sari
# Mini Project 4

from django.contrib import admin

from .models import Product, CheckOut, CheckIn


class ProductAdmin(admin.ModelAdmin):
    list_display = ["asset_tag", "name", "make", "model", "serial_number","note"]
    list_filter = ["make", "name"]


admin.site.register(Product, ProductAdmin)
admin.site.register(CheckOut)
admin.site.register(CheckIn)
