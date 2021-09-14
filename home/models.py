from django.db import models

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

class CategoriesHasProducts(models.Model):
    categories = models.OneToOneField(Categories, models.DO_NOTHING, blank=True, null=True)
    products = models.OneToOneField('Products', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'categories_has_products'

    def __str__(self):
        return self.categories

class Customers(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'customers'

    def __str__(self):
        return self.fname

class CustomersHasAddresses(models.Model):
    id=models.AutoField(primary_key=True)
    customer = models.OneToOneField(Customers, models.DO_NOTHING, blank=True, null=True)
    address = models.OneToOneField(Address, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'customers_has_addresses'
    
    '''def __str__(self):
        return self.customer'''

class CustomersHasFavoriteProducts(models.Model):
    customers = models.OneToOneField(Customers, models.DO_NOTHING, primary_key=True)
    products = models.OneToOneField(Brand, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'customers_has_favorite_products'

    def __str__(self):
        return self.customers

class Items(models.Model):
    id = models.IntegerField(primary_key=True)
    productions_date = models.DateField(blank=True, null=True)
    products = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'items'

    def __str__(self):
        return self.products

class OrderHasItems(models.Model):
    order = models.OneToOneField('Orders', models.DO_NOTHING, primary_key=True)
    items = models.OneToOneField(Items, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'order_has_items'

    def __str__(self):
        return self.order

class Orders(models.Model):
    id = models.IntegerField(primary_key=True)
    purchase_date = models.DateField(blank=True, null=True)
    customers = models.ForeignKey(Customers, models.DO_NOTHING)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return self.id

class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    about = models.CharField(max_length=1000, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    warranty = models.IntegerField(blank=True, null=True)
    brand = models.ForeignKey(Brand, models.DO_NOTHING)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name

class Reviews(models.Model):
    customers = models.OneToOneField(Customers, models.DO_NOTHING, primary_key=True)
    ratings = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    products = models.OneToOneField(Products, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'reviews'

    def __str__(self):
        return self.customers