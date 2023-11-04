from django.contrib import admin
from .models import Product
from .models import CheckOut
from .models import CheckIn


admin.site.register(Product)
admin.site.register(CheckOut)
admin.site.register(CheckIn)

