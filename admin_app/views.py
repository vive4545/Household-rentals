from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from admin_app import forms
from admin_app import models
from django.core.paginator import Paginator
from household_app.models import rental
from client_app.models import clientdetails
from django.contrib import messages
# Create your views here.

def profileview(request):
    if request.method == 'post':
        form = forms.CustomPasswordChangeForm(request.user,request.post)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Password change successfuly")
            return redirect(profileview)
        else:
            print(form.errors)
            messages.error(request,"")
    return render(request,'main/profile.html')


def registerview(request):
    if request.method == 'POST':
        if request.POST.get('password') == request.POST.get('password1'):
            try:
                User.objects.get(username=request.POST.get('username'))
                messages.error(request,"username already set")
            except:
                User.objects.create_user(username=request.POST.get('username'),
                                         password=request.POST.get('password'))
                messages.success(request,"User Registered Successfully")
                return redirect(loginview)
        else:
            messages.error(request,"Passwords do not match")
    return render(request,'main/register.html')

def loginview(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect(indexview)
        else:
            return HttpResponse("user not found")
    return render(request,'main/login.html')

def indexview(request):
    return render(request,'main/index.html')

def generaltableview(request):
    data = rental.objects.all()
    paginator =Paginator(data,4)
    page_number = request.GET.get('page')
    page_obj= paginator.get_page(page_number)
    context = {'data':page_obj,'page_number':page_number}
    return render(request, 'main/generaltable.html',context=context)

def elementsview(request):
    form = forms.customerform(request.POST)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect(generaltableview)
    else:
        print(form.errors)
    return render(request,'main/elements.html')

def logoutview(request):
    logout(request)
    return redirect(loginview)

def deletecustomer(request,id):
    data = rental.objects.get(id=id)
    print(data.delete())
    return redirect(generaltableview)

def editcustomer(request,id):
    data = rental.objects.get(id=id)
    context = {'data':data}
    return render(request,'main/editform.html',context=context)

def updatecustomer(request,id):
    data = rental.objects.get(id=id)
    form = forms.customerform(request.POST,instance=data)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        return redirect(generaltableview)
    else:
        print(form.errors)
    return render(request, 'main/editform.html')

#----------------(Client update,delete and create)------------------------#


def datatableview(request):
    data = clientdetails.objects.all()
    paginator =Paginator(data,5)
    page_number = request.GET.get('page')
    page_obj= paginator.get_page(page_number)
    context = {'data':page_obj,'page_number':page_number}
    return render(request,'main/data_tables.html', context=context)

def editclient(request,id):
    data = clientdetails.objects.get(id=id)
    context = {'data':data}
    return render(request,'main/editclient.html',context=context)

def updateclient(request,id):
    data = clientdetails.objects.get(id=id)
    form = forms.clientforms(request.POST,request.FILES,instance=data)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect(datatableview)
        else:
            print(form.errors)
    return render(request,'main/editclient.html')




def deleteclient(request,id):
    data = clientdetails.objects.get(id=id)
    data.delete()
    return redirect(datatableview)


#------------------------(Forget password)------------------------

def c_view(request):
    form = forms.CouponForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect(c_view)
    else:
        print(form.errors)
    return render(request,'main/coupon.html')

def deletecoupon(request,id):
    data = models.Coupon.objects.get(id=id)
    data.delete()
    return redirect(c_view)

def couponview(request):
    data = models.Coupon.objects.all()
    paginator =Paginator(data,3)
    page_number = request.GET.get('page')
    page_obj= paginator.get_page(page_number)
    context = {'data':page_obj,'page_number':page_number}
    return render(request,'main/couponview.html', context=context)

def updatecoupon(request,id):
    data = models.Coupon.objects.get(id=id)
    form = forms.CouponForm(request.POST,request.FILES,instance=data)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect(couponview)
        else:
            print(form.errors)
    return render(request,'main/couponview.html')

def editcoupon(request,id):
    data = models.Coupon.objects.get(id=id)
    context = {'data':data}
    return render(request,'main/editcoupon.html',context=context)

