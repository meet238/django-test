from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    sub_category = models.ManyToManyField(
        to='SubCategory',
        related_name='sub_category',
    )

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)

    class Meta:
        db_table = 'sub_category'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    product_code = models.PositiveIntegerField(null=False, blank=False, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    category = models.ForeignKey(
        to='Category',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    manufacture_date = models.DateField(null=False, blank=False)
    expiry_date = models.DateField(null=False, blank=False)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name
