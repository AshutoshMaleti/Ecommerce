from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *

# Create your views here.
def AddToCart(request, pk):
    productId=get_object_or_404(Products, id=pk)
    orderItem=OrderHasProduct.objects.filter(productId[0])
    orderQs=Orders.objects.filter(customerId=request.customer.id, status=False)
    if orderQs.exists():
        item=orderItem[0]
        if item in orderQs[0]:
            orderQs[0]['']
    #return HttpResponse('This is Add Items page.')

@api_view(['POST'])
def Order(request, pk):
    serializer=OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response('Order placed!')