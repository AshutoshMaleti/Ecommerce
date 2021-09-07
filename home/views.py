from django.shortcuts import render, redirect

#from django.contrib.auth import logout, login, authenticate

# Create your views here.
def index(request):
    return render(request, 'base.html')

def brands(request):
    return render(request, 'brands.html')

def signin(request):
    pass

def signup(request):
    pass