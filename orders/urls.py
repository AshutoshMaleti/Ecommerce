from django.urls import path
from orders import views

urlpatterns = [
    path('add-to-cart/<str:pk>/', views.AddToCart, name='AddToCart'),
    path('remove-from-cart/<str:pk>/', views.RemoveFromCart, name='RemoveFromCart'),
    path('delete-from-cart/<str:pk>/', views.DeleteItem, name='DeleteItem'),
    path('order-summary/', views.OrderSummary, name='OrderSummary'),
    path('order/', views.Orders, name='Order')
]