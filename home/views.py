from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *
from .models import *

# Create your views here.
@api_view(['GET'])
def Home(request):
    api_urls={
        'home':'/',
        'brands':'/brands/',

        'enter customer details':'/customers-details/',
        'show customer details':'/get-customers-details/<str:pk>/',
        'update customer details':'/update-customers-details/<str:pk>/',
        'delete customer details':'/delete-customers-details/<str:pk>/',

        'add address':'/add-address/<str:pk>/',

        'add product of id pk to cart':'/add-to-cart/<str:pk>/',
        'remove a product of id pk from cart':'remove-from-cart/<str:pk>/',
        'delete a product of id pk from cart':'delete-from-cart/<str:pk>/',
        'get order summary':'add-to-cart/<str:pk>/',

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

@api_view(['POST'])
def CustomerDetails(request):
    serializer=CustomersSerializer(data=request.data)
    user=request.user
    Customers(user=user, fname=serializer.initial_data['fname'], lname=serializer.initial_data['lname'], email=serializer.initial_data['email']).save()

    response=Customers.objects.last()
    return Response(serializer.initial_data)
#{"fname":"","lname":"","email":""}

@api_view(['GET'])
def GetCustomersDetails(request, pk):
    details=Customers.objects.get(id=pk)
    serializer=CustomersSerializer(details, many=False)

    return Response(serializer.data)

@api_view(['PATCH'])
def UpdateCustomersDetails(request, pk):
    instance=Customers.objects.get(id=pk)
    print(instance)
    serializer=CustomersSerializer(instance, data=request.data)
    print(serializer)
    print(serializer.is_valid())
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteCustomer(request, pk):
    customer=Customers.objects.get(id=pk)
    customer.delete()

    return Response('Customer deleted!')

@api_view(['POST'])
def SetAddress(request, pk):
    address=AddressSerializer(data=request.data)

    Address.objects.get_or_create(state=address.initial_data['state'], city=address.initial_data['city'], street=address.initial_data['street'], number=address.initial_data['number'])

    customerid=Customers.objects.get(id=pk)
    addressid=Address.objects.filter(state=address.initial_data['state'], city=address.initial_data['city'], street=address.initial_data['street'], number=address.initial_data['number'])

    CustomersHasAddresses(customer=customerid, address=addressid[0]).save()
    return Response('Address added')
#{"state":"7","city":"7","street":"7","number":"7"}

@api_view(['POST'])
def WriteReviews(request, pk):
    customerQs = Customers.objects.get(user=request.user)
    productQs = Products.objects.get(id=pk)

    serializer=ReviewsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(customer=customerQs, product=productQs)

    return Response(serializer.data)
#{"ratings":"3","description":"meh"}

@api_view(['GET'])
def ReadReviews(request, pk):
    reviewId=Reviews.objects.filter(product__id=pk)
    reviews = ReviewsSerializer(reviewId, many=True)

    return Response(reviews.data)

@api_view(['PATCH'])
def UpdateReviews(request, pk):
    instance = Reviews.objects.get(id=pk)
    serializer=ReviewsSerializer(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteReviews(request, pk):
    review = Reviews.objects.get(id=pk)
    review.delete()
    
    return Response('Review deleted.')

@api_view(['POST'])
def AddToFav(request, pk):
    productQs = get_object_or_404(Products, id=pk)
    customerQs = Customers.objects.filter(user=request.user)

    CustomersHasFavoriteProducts(customers=customerQs[0], products=productQs).save()

    return Response('Product added to faviorites.')

@api_view(['DELETE'])
def RemoveFromFav(request, pk):
    productQs = get_object_or_404(Products, id=pk)
    customerQs = Customers.objects.filter(user=request.user)

    CustomersHasFavoriteProducts.objects.filter(customers=customerQs[0], products=productQs).delete()

    return Response('Removed from Favourites!')
