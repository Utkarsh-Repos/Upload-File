from django.db import models
from decimal import Decimal


class Product(models.Model):
    product_id = models.CharField(max_length=50, primary_key=True)
    product_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    quantity_sold = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    review_count = models.IntegerField()

    def __str__(self):
        return self.product_name
