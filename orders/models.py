from django.db import models
from home.models import Customers, Products

# Create your models here.
'''class Items(models.Model):
    id = models.IntegerField(primary_key=True)
    productionDate = models.DateField(blank=True, null=True)
    products = models.ForeignKey(Products, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'items'

    def __str__(self):
        return self.id'''

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    orderDate = models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)
    customer = models.ForeignKey(Customers, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return str(self.id)

class OrderHasProduct(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Orders, models.SET_NULL, unique=False, blank=True, null=True)
    orderProducts = models.ForeignKey(Products, models.SET_NULL, unique=False, blank=True, null=True)
    quantity=models.IntegerField(default=1)

    class Meta:
        db_table = 'order_has_products'

    def __str__(self):
        return str(self.order)