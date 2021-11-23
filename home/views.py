from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.db import IntegrityError

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *
from .models import *

# Create your views here.
@api_view(['GET'])
def Home(request):
    api_urls={
        'home':'/',

        'signup':'/account/signup/',
        'signin':'/account/signin/',
        'signout':'/account/signout/',

        'brands':'/brands/',

        'enter customer details':'/add-customers-details/',
        'show customer details':'/get-customers-details/',
        'update customer details':'/update-customers-details/',
        'delete customer details':'/delete-customers-details/',

        'add address for current user':'/add-address/',

        'add product of id pk to cart':'/orders/add-to-cart/<str:pk>/',
        'remove a product of id pk from cart':'/orders/remove-from-cart/<str:pk>/',
        'delete a product of id pk from cart':'/orders/delete-from-cart/<str:pk>/',
        'get order summary':'/orders/add-to-cart/<str:pk>/',

        'write a review for a product with id=pk':'write-reviews/<str:pk>/',
        'read all the reviews for a product with id=pk':'read-reviews/<str:pk>/',
        'update a review with review id=pk':'update-reviews/<str:pk>/',
        'delete a review with review id=pk':'delete-reviews/<str:pk>/',

        'add a product of id=pk to favourites':'add-to-favourite/<str:pk>/',
        'remove a product of id=pk from favourites':'remove-from-favourite/<str:pk>/'
    }

    return Response(api_urls)

def Brands(request):
    return render(request, 'brands.html')

@login_required(login_url='/account/signin/')
@api_view(['POST'])
def CustomerDetails(request):
    try:
        serializer=CustomersSerializer(data=request.data)
        user=request.user
        
        Customers(user=user, fname=serializer.initial_data['fname'], lname=serializer.initial_data['lname'], email=serializer.initial_data['email']).save()

        response=Customers.objects.last()
        return Response(serializer.initial_data)

    except IntegrityError:
        return Response('Customer details already exists for current user, try updating.')
#{"fname":"","lname":"","email":""}

@login_required(login_url='/account/signin/')
@api_view(['GET'])
def GetCustomersDetails(request):
    details=Customers.objects.get(user=request.user)
    serializer=CustomersSerializer(details, many=False)

    return Response(serializer.data)

@login_required(login_url='/account/signin/')
@api_view(['PATCH'])
def UpdateCustomersDetails(request):
    instance=Customers.objects.get(user=request.user)
    serializer=CustomersSerializer(instance, data=request.data)

    if serializer.is_valid():
        serializer.save()
    #print(serializer.errors) this is used to see the error details in serializers.
    #patch requests only works here wouldn't work until you provide a first name because it's a required field.
    
    return Response(serializer.data)

@login_required(login_url='/account/signin/')
@api_view(['DELETE'])
def DeleteCustomer(request):
    customer=Customers.objects.get(user=request.user)
    customer.delete()

    return Response('Customer deleted!')

@login_required(login_url='/account/signin/')
@api_view(['POST'])
def SetAddress(request):
    address=AddressSerializer(data=request.data)

    Address.objects.get_or_create(state=address.initial_data['state'], city=address.initial_data['city'], street=address.initial_data['street'], number=address.initial_data['number'])

    customerid=Customers.objects.get(user=request.user)
    addressid=Address.objects.filter(state=address.initial_data['state'], city=address.initial_data['city'], street=address.initial_data['street'], number=address.initial_data['number'])

    CustomersHasAddresses(customer=customerid, address=addressid[0]).save()
    return Response('Address added')
#{"state":"7","city":"7","street":"7","number":"7"}

@login_required(login_url='/account/signin/')
@api_view(['POST'])
def WriteReviews(request, pk):
    customerQs = Customers.objects.get(user=request.user)
    productQs = Products.objects.get(id=pk)

    serializer=ReviewsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(customer=customerQs, product=productQs)

    return Response(serializer.data)
#{"ratings":"3","description":"meh"}

@login_required(login_url='/account/signin/')
@api_view(['GET'])
def ReadReviews(request, pk):
    reviewId=Reviews.objects.filter(product__id=pk)
    reviews = ReviewsSerializer(reviewId, many=True)

    return Response(reviews.data)

@login_required(login_url='/account/signin/')
@api_view(['PATCH'])
def UpdateReviews(request, pk):
    try:
        instance = Reviews.objects.get(customer__user=request.user, id=pk)
        serializer=ReviewsSerializer(instance, data=request.data)
        
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    except:
        return Response("reviews with given id doesn't exists for current user.")

@login_required(login_url='/account/signin/')
@api_view(['DELETE'])
def DeleteReviews(request, pk):
    try:
        review = Reviews.objects.get(customer__user=request.user, id=pk)
        review.delete()
        
        return Response('Review deleted.')
    except:
        return Response("you can't delete reviews not created by you.")

@login_required(login_url='/account/signin/')
@api_view(['POST'])
def AddToFav(request, pk):
    productQs = get_object_or_404(Products, id=pk)
    customerQs = Customers.objects.filter(user=request.user)

    CustomersHasFavoriteProducts(customers=customerQs[0], products=productQs).save()

    return Response('Product added to faviorites.')

@login_required(login_url='/account/signin/')
@api_view(['DELETE'])
def RemoveFromFav(request, pk):
    productQs = get_object_or_404(Products, id=pk)
    customerQs = Customers.objects.filter(user=request.user)

    CustomersHasFavoriteProducts.objects.filter(customers=customerQs[0], products=productQs).delete()

    return Response('Removed from Favourites!')
