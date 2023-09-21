from django.contrib import admin
from .models.products import Product
from .models.category import Category
from .models.customer import Customer
from .models.order import Order
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['product_name','product_price','product_description','category']

admin.site.register(Product,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
