from django.db import models
from rest_framework import serializers
from .models import Customers, Orders

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['fname', 'lname', 'email', 'address']

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields='__all__'