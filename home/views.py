from django.shortcuts import render#, redirect

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def brands(request):
    return render(request, 'brands.html')

@api_view(['POST'])
def customerDetails(request):
    serializer=CustomersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
#{"fname":"mohan","lname":"gandhi","email":"gandhi@rediff.com","address":"somewhere in south africa"}
