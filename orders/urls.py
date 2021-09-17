from django.urls import path
from orders import views

urlpatterns = [
    path('add-to-cart/<str:pk>/', views.AddToCart, name='AddToCart'),
    path('order/', views.Orders, name='Order')
]