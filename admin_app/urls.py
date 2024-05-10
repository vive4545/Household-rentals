from django.contrib import admin
from django.urls import path,include
from admin_app import views

urlpatterns = [
    path('index/',views.indexview,name='a_index'),

    path('register/',views.registerview,name='register'),

    path('profile/',views.profileview,name='profile'),

    path('login/',views.loginview,name='login'),

    path('logout/',views.logoutview,name='logout'),

    path('elements/',views.elementsview,name='elements'),

    path('generaltable/',views.generaltableview,name='generaltable'),

    path('deletecustomer/<int:id>/',views.deletecustomer,name='deletecustomer'),

    path('editcustomer/<int:id>/',views.editcustomer,name='editcustomer'),

    path('updatecustomer/<int:id>/',views.updatecustomer,name='updatecustomer'),
    

#---------------------------(Clients details)-------------------#    

    path('updateclient/<int:id>/',views.updateclient,name='updateclient'),

    path('deleteclient/<int:id>/',views.deleteclient,name='deleteclient'),

    path('datatables/',views.datatableview,name='datatable'),

    path('editclient/<int:id>/',views.editclient,name='editclient'),

    path('coupons/',views.c_view,name='coupons'),

    path('deletecoupon/<int:id>/',views.deletecoupon,name='couponsview'),

    path('couponsview',views.couponview,name='couponsview'),

    path('updatecoupons/<int:id>/',views.updatecoupon,name ='updatecoupon'),

    path('editcoupon/<int:id>',views.editcoupon,name ='editcoupon'),

]