from django.contrib import admin
from django.urls import path,include
from household_app import views

urlpatterns = [
    path('index/',views.indexview,name='index'),

    path('about/',views.aboutview,name='about'),

    path('contact/',views.contactview,name='contact'),

    path('forms/',views.formsview,name='forms'),

    path('r_login/',views.r_loginview,name='r_login'),

    path('r_logout/',views.r_logoutview,name='r_logout'),

    path('r_register/',views.r_registerview,name='r_register'),

    path('productrent/',views.product_rent,name='productrent'),

    path('productdetails/',views.productdetails,name='productdetails'),

    path('productview/',views.productview,name='productview'),

    path('r_invoice/',views.invoiceview,name='r_invoice'),

    path('delete/<int:id>/',views.deleteimg,name='delete'),

    path('edit/<int:id>/',views.editimage,name='edit'),

    path('update/<int:id>/',views.updateimage,name='updateimage'),


    







]