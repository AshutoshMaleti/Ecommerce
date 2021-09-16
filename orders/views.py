from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *

# Create your views here.
def AddToCart(request):
    if request.user.is_authenticated:
        print('inside is_authenticated')
        user = request.user.id
        print(user)
        customerQs = Customers.objects.filter(user=user).first()
        print(customerQs)
        #print(customerQs[0]['id'])
        orderQs = Orders.objects.get_or_create(customer=customerQs, status=False)
        print(orderQs)
        orderProduct=orderQs.OrderHasProduct_set.all()
        print(orderProduct)

        '''customer = request.user.customer
        order = Orders.objects.get_or_create(customer)
        product = order.orderhasproduct_set.all()'''
    else:
        items = []
        order = {'items':items}

    return Response('chal rha hai')

'''def AddToCart(request, pk):
    productId = get_object_or_404(Products, id=pk)
    orderItem = OrderHasProduct.objects.filter(productId)
    orderQs = Orders.objects.filter(customerId=request.User, status=False)
    if orderQs.exists():
        item = orderItem[0]
        if item in orderQs[0]:
            orderItem[0]['quantity'] += 1
            orderQs.save()
        else:
            orderItem = OrderHasProduct.objects.create(order=productId)
    return HttpResponse('This is Add Items page.')'''

@api_view(['POST'])
def Order(request, pk):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response('Order placed!')