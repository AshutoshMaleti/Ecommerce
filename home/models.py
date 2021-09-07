from django.db import models
from .models import *


class Address(models.Model):
    id = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    street = models.CharField(max_length=45, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'address'


class Brand(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'brand'


class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    descriptions = models.CharField(max_length=250, blank=True, null=True)
    categories = models.ForeignKey('self', models.DO_NOTHING, related_name='+', blank=True, null=True)

    class Meta:
        db_table = 'categories'


class CategoriesHasProducts(models.Model):
    categories = models.OneToOneField(Categories, models.DO_NOTHING, primary_key=True)
    products = models.OneToOneField('Products', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'categories_has_products'


class Customers(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    address = models.ForeignKey(Address, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'customers'


class CustomersHasFavoriteProducts(models.Model):
    customers = models.OneToOneField(Customers, models.DO_NOTHING, primary_key=True)
    products = models.OneToOneField(Brand, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'customers_has_favorite_products'


class Items(models.Model):
    id = models.IntegerField(primary_key=True)
    productions_date = models.DateField(blank=True, null=True)
    products = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'items'


class OrderHasItems(models.Model):
    order = models.OneToOneField('Orders', models.DO_NOTHING, primary_key=True)
    items = models.OneToOneField(Items, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'order_has_items'


class Orders(models.Model):
    id = models.IntegerField(primary_key=True)
    purchase_date = models.DateField(blank=True, null=True)
    customers = models.ForeignKey(Customers, models.DO_NOTHING)

    class Meta:
        db_table = 'orders'


class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    about = models.CharField(max_length=1000, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    warranty = models.IntegerField(blank=True, null=True)
    brand = models.ForeignKey(Brand, models.DO_NOTHING)

    class Meta:
        db_table = 'products'


class Reviews(models.Model):
    customers = models.OneToOneField(Customers, models.DO_NOTHING, primary_key=True)
    ratings = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    products = models.OneToOneField(Products, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'reviews'
