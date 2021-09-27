
from django.urls import path
from accounts import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/',views.signout, name='signout'),
]