from django.shortcuts import render

#from rest_framework import viewsets
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
#{"fname":"mohan","lname":"gandhi","email":"gandhi@rediff.com","address":"somewhere in south africa"}

'''class CustomerDetails(viewsets.ModelViewSet):
    quaryset=Customers.objects.all()
    serializer=CustomersSerializer'''

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