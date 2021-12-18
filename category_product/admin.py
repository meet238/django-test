from django.contrib import admin

# Register your models here.
from category_product.models import Category, SubCategory, Product


class AdminProduct(admin.ModelAdmin):
    model = Product
    readonly_fields = [
        'crated_at', 'updated_at'
    ]


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product, AdminProduct)
