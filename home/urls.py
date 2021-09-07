from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brands', views.brands, name='brands'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
]