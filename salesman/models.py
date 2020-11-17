from django.utils import timezone
from django.db import models


class Products(models.Model):
    product_name = models.CharField(max_length=100)
    SKU = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField()
    product_category = models.CharField(max_length=100)
    product_stock = models.IntegerField(blank=False, null=False)
    product_location = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    product_updated = models.DateTimeField(default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.product_updated = timezone.now()
        self.save()

    def __str__(self):
        return str(self.product_name)

    class Meta:
        verbose_name_plural = "products"


# Create your models here.
class Customer(models.Model):
    cust_name = models.CharField(max_length=50)
    organization = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    bldgroom = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    account_number = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.cust_name)

    class Meta:
        verbose_name_plural = "customers"
