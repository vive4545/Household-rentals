from django.contrib import admin
from django.urls import path,include
from client_app import views

urlpatterns = [
    path('clientindex/',views.clientindexview,name='c_index'),

    path('clientshop/',views.clientshop,name='c_shop'),

    path('c_login/',views.c_loginview,name='c_login'),

    path('c_logout/',views.c_logoutview,name='c_logout'),

    path('c_register/',views.c_registerview,name='c_register'),

    path('c_details/',views.c_detailsview,name='c_details'),

    path('c_about/',views.c_aboutview,name='c_about'),

    path('c_error/',views.c_errorview,name='c_error'),

    path('c_singleproduct/',views.c_singleview,name='c_singleproduct'),

    path('c_cart/',views.c_cartview,name='c_cartview'),

    path('c_checkout/<int:id>/',views.c_checkoutview,name='c_checkout'),

    path('c_contact/',views.c_contactview,name='c_contact'),

    path('item_clear/<int:id>/',views.item_clear,name='item_clear'),

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),

    path('cart/edit/<int:id>/', views.cart_edit, name='cart_edit'),

    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),

    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),

    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),

    path('c_payment/', views.payments, name='payment'),

    path('searchview/', views.searchview, name='searchview'),

    path('forgetpassword/',views.forget_password,name='forgetpassword'),

    path('applycoupan/',views.applycoupan,name='applycoupan'),


        
         










]