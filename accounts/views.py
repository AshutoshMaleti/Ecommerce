from django.shortcuts import render, redirect

from .forms import CreateUser
from django.contrib.auth import login, logout, authenticate

from django.contrib import messages

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUser()
        if request.method=='POST':
            form =CreateUser(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request, 'Account was successfully created for '+user)

                return redirect('signin')

        context = {'form':form}
        return render(request, 'signup.html', context)


def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request, username=username,password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('signup')

        return render(request, 'signin.html')


def signout(request):
    logout(request)
    return render(request, 'home.html')