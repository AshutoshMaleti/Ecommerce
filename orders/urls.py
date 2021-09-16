from django.urls import path
from orders import views

urlpatterns = [
    path('add-to-cart/', views.AddToCart, name='AddToCart'),
    path('order/<str:pk>/', views.Orders, name='Order')
]