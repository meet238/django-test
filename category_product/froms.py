from django import forms

from category_product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_code', 'price', 'category', 'manufacture_date', 'expiry_date']
