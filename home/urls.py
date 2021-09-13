from django.urls import path#, include
from home import views
'''from rest_framework import routers

router=routers.DefaultRouter()
router.register('customers-details',views.CustomerDetails,basename='CustomerDetails')'''

urlpatterns = [
    path('', views.Home, name='Home'),
    #path('', include(router.urls)),
    path('brands/', views.Brands, name='Brands'),
    path('customers-details/', views.CustomerDetails, name='CustomerDetails'),
    path('get-customers-details/<str:pk>/', views.GetCustomersDetails, name='GetCustomersDetails'),
    path('update-customers-details/<str:pk>/', views.UpdateCustomersDetails, name='UpdateCustomersDetails'),
    path('delete-customers-details/<str:pk>/', views.DeleteCustomer, name='DeleteCustomer'),
    path('add-address/<str:pk>/', views.SetAddress, name='SetAddress'),
]