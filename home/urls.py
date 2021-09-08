from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('brands', views.brands, name='brands'),
    path('customersDetails', views.customerDetails, name='customerDetails')
]