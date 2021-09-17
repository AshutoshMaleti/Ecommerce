from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *

# Create your views here.
@api_view(['POST'])
def AddToCart(request, pk):
    if request.user.is_authenticated:
        user = request.user.id
        customerQs = Customers.objects.filter(user=user)    #output - <QuerySet [{'id': 18, 'user_id': 9, 'fname': 'ashu', 'lname': 'maleti', 'email': 'blah'}]> a queryset something like this.
        productQs = get_object_or_404(Products, id=pk)  #output - iphone
        order = Orders.objects.get_or_create(customer=customerQs[0])    #creates order if not present with associated customer passed.

        orderHasItems = OrderHasProduct.objects.filter(order__customer__fname=customerQs[0], order__status=False, products__name=productQs)
        
        if orderHasItems.exists():
            incrementor = orderHasItems[0].quantity+1
            orderHasItems.update(quantity=incrementor)
        else:
            OrderHasProduct.objects.create(order=order[0], products=productQs).save()

        return Response('Added to cart!')

    else:
        items = []
        order = {'items':items}

    return Response('chal rha hai')


@api_view(['POST'])
def Order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.data.status=True
        serializer.save()

    return Response('Order placed!')