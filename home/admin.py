from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Address)
admin.site.register(Customers)
admin.site.register(CustomersHasAddresses)
admin.site.register(Brand)
admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(CategoriesHasProducts)
admin.site.register(CustomersHasFavoriteProducts)
admin.site.register(Reviews)