from rest_framework import serializers
from .models import Address, Customers, Reviews

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

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id', 'ratings', 'description']