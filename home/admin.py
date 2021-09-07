from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Address)
admin.site.register(Customers)
admin.site.register(Brand)
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(Items)
admin.site.register(Categories)
admin.site.register(CategoriesHasProducts)
admin.site.register(CustomersHasFavoriteProducts)
admin.site.register(OrderHasItems)
admin.site.register(Reviews)
