from django.db import models
from .category import Category

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=200)
    product_price = models.IntegerField(default=1)
    product_images = models.ImageField(upload_to="uploads/products")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)

    @staticmethod
    def Get_all_products_by_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.Get_all_products()

    @staticmethod
    def Get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)

