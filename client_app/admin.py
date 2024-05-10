from django.contrib import admin
from client_app.models import clientdetails ,contactdetails, customerproduct,billingproduct,FinalOrder,ConfirmOrder
# Register your models here.


@admin.register(clientdetails)
class clientdetails(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'address')
@admin.register(contactdetails)
class contactdetails(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'subject','message')
@admin.register(customerproduct)
class customerproduct(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'productimage', 'quantity')
@admin.register(billingproduct)
class billingproduct(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'address', 'phone','user',)

@admin.register(FinalOrder)
class FinalOrderadmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total')

@admin.register(ConfirmOrder)
class ConfirmOrderadmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'final', 'product', 'quantity','subtotal')

