from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *
from .models import *

# Create your views here.
@api_view(['GET'])
def Home(request):
    api_urls={
        'create customer':'customers-details',
        'show details':'get-customers-details/<str:pk>',
        'update details':'update-customers-details/<str:pk>',
        'delete customer details':'delete-customers-details/<str:pk>',
    }

    return Response(api_urls)

def Brands(request):
    return render(request, 'brands.html')

@api_view(['POST'])
def CustomerDetails(request):
    serializer=CustomersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
#{"fname":"","lname":"","email":""}

@api_view(['GET'])
def GetCustomersDetails(request, pk):
    details=Customers.objects.get(id=pk)
    serializer=CustomersSerializer(details,many=False)
    
    return Response(serializer.data)

@api_view(['POST'])
def UpdateCustomersDetails(request,pk):
    details=Customers.objects.get(id=pk)
    serializer=CustomersSerializer(instance=pk,data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteCustomer(pk):
    customer=Customers.objects.get(id=pk)
    customer.delelte()

    return Response('Customer deleted!')

@api_view(['POST'])
def SetAddress(request,pk):
    address=AddressSerializer(data=request.data)

    Address.objects.get_or_create(state=address.initial_data['state'], city=address.initial_data['city'], street=address.initial_data['street'], number=address.initial_data['number'])

    customerid=Customers.objects.get(id=pk)
    addressid=Address.objects.filter(state=address.initial_data['state'], city=address.initial_data['city'], street=address.initial_data['street'], number=address.initial_data['number'])

    CustomersHasAddresses(customer=customerid, address=addressid[0]).save()

    

    '''print(serializer.is_valid())
    if serializer.is_valid():    
        serializer.save()'''
    return Response('Address added')
#{"state":"7","city":"7","street":"7","number":"7"}