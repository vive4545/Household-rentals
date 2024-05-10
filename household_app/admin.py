from django.contrib import admin
from household_app.models import rental,product_rent
# Register your models here.

@admin.register(rental)
class rental(admin.ModelAdmin):
    list_display = ('id', 'user', 'address','phone', 'email')

@admin.register(product_rent)
class product_rent(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'productType','boughtdate', 'image','price')