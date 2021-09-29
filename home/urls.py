from django.urls import include, path
from home import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('brands/', views.Brands, name='Brands'),

    path('add-customers-details/', views.CustomerDetails, name='CustomerDetails'),
    path('get-customers-details/', views.GetCustomersDetails, name='GetCustomersDetails'),
    path('update-customers-details/', views.UpdateCustomersDetails, name='UpdateCustomersDetails'),
    path('delete-customers-details/', views.DeleteCustomer, name='DeleteCustomer'),
    
    path('add-address/<str:pk>/', views.SetAddress, name='SetAddress'),

    path('write-reviews/<str:pk>/', views.WriteReviews, name='WriteReviews'),
    path('read-reviews/<str:pk>/', views.ReadReviews, name='ReadReviews'),
    path('update-reviews/<str:pk>/', views.UpdateReviews, name='UpdateReviews'),
    path('delete-reviews/<str:pk>/', views.DeleteReviews, name='DeleteReviews'),

    path('add-to-favourite/<str:pk>/', views.AddToFav, name='AddToFav'),
    path('remove-from-favourite/<str:pk>/', views.RemoveFromFav, name='RemoveFromFav'),
]