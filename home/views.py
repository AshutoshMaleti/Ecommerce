from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def brands(request):
    return render(request, 'brands.html')