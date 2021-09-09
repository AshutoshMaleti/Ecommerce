from django.db import models
from rest_framework import serializers
from .models import Address, Customers, Orders

class CustomersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customers
        fields = ['fname', 'lname', 'email', 'address']

    def to_representation(self,instance):
        response=super().to_representation(instance)
        response['address']=AddressSerializer(instance.address).data
        return response

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields='__all__'

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields='__all__'