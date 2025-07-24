from django.contrib import admin
from .models import Category, Customers, Product, Order
# Register your models here.

admin.site.register(Category)
admin.site.register(Customers)
admin.site.register(Product)
admin.site.register(Order)