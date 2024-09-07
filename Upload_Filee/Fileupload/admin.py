from django.contrib import admin
from .models import Product
class ProductAdmin(admin.ModelAdmin):
    class Meta:
        field = '__all__'
admin.site.register(Product, ProductAdmin)
# Register your models here.
