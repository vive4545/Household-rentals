from django.contrib import admin
from admin_app.models import customer,client_model,Coupon
# Register your models here.

# admin.site.register(customer)

@admin.register(customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id',  'email', 'phone', 'address')

@admin.register(client_model)
class clientadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'address','proof')

@admin.register(Coupon)

class couponadmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'discount', 'expiry_date')