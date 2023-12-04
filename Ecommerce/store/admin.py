from django.contrib import admin
from . models import Category,Product,SubCategory,ProductSegment,ProductSeries
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(SubCategory)
admin.site.register(ProductSeries)
admin.site.register(ProductSegment)