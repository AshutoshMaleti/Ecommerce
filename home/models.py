from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

#Create your models here.
class Address(models.Model):
    state = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    street = models.CharField(max_length=45, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'address'

    def __str__(self):
        return self.city

class Brand(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'brand'

    def __str__(self):
        return self.name

class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    descriptions = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name

class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    about = models.CharField(max_length=1000, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    #warranty = models.IntegerField(blank=True, null=True)
    brand = models.ForeignKey(Brand, models.DO_NOTHING)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name

class CategoriesHasProducts(models.Model):
    categories = models.OneToOneField(Categories, models.DO_NOTHING, blank=True, null=True)
    products = models.OneToOneField(Products, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'categories_has_products'

    def __str__(self):
        return self.categories

class Customers(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'customers'

    def __str__(self):
        return self.fname

class CustomersHasAddresses(models.Model):
    id=models.AutoField(primary_key=True)
    customer = models.OneToOneField(Customers, models.DO_NOTHING, unique=False, blank=True, null=True)
    address = models.OneToOneField(Address, models.DO_NOTHING, unique=False, blank=True, null=True)

    class Meta:
        db_table = 'customers_has_addresses'

    def __str__(self):
        return str(self.customer)

class CustomersHasFavoriteProducts(models.Model):
    customers = models.OneToOneField(Customers, models.DO_NOTHING, primary_key=True)
    products = models.OneToOneField(Brand, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'customers_has_favorite_products'

    def __str__(self):
        return self.customers

class Reviews(models.Model):
    reviewId=models.AutoField(primary_key=True)
    customers = models.OneToOneField(Customers, models.DO_NOTHING)
    products = models.OneToOneField(Products, models.DO_NOTHING, blank=True, null=True)
    ratings = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)], blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'reviews'

    def __str__(self):
        return self.customers