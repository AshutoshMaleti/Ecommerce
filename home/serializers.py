from rest_framework import serializers
from .models import Address, Customers, Orders, CustomersHasAddresses

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id', 'fname', 'lname', 'email']
    '''
    def to_representation(self,instance):
        response=super().to_representation(instance)
        response['address']=AddressSerializer(instance.address).data
        return response'''

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'state', 'city', 'street', 'number']

class CustomerHasAddress(serializers.ModelSerializer):
    class Meta:
        model = CustomersHasAddresses
        fields=['id', 'customer', 'address']

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'