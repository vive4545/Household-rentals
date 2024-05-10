from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from household_app import forms
from household_app import models
from django.contrib import messages

# Create your views here.


def indexview(request):
    return render(request,'rentals/index.html')


def invoiceview(request):
    return render(request,'rentals/invoice.html')



def editimage(request,id):
    data = models.product_rent.objects.get(id=id)
    context = {'data':data}
    return render(request,'rentals/productedit.html',context=context)



def updateimage(request,id):
    data = models.product_rent.objects.get(id=id)
    form = forms.product_rentform(request.POST,instance=data)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        return redirect(productdetails)
    else:
        print(form.errors)
    return render(request, 'rentals/productedit.html')


def deleteimg(request,id):
    data = models.product_rent.objects.get(id=id)
    print(data.delete())
    return redirect(productview)


def productview(request):
    data = models.product_rent.objects.all()
    context = {'data':data}
    return render(request, 'rentals/productview.html',context=context)


def productdetails(request):
    data = models.product_rent.objects.all()
    context = {'data':data}
    return render(request,'rentals/productdetails.html',context=context)


def product_rent(request):
    if request.method == "POST":
        form = forms.product_rentform(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect(productview)
        else:
            return redirect(forms.error)
    return render(request,'rentals/productrent.html')

def aboutview(request):
    return render(request,'rentals/about.html')

def contactview(request):
    return render(request,'rentals/contact.html')



def formsview(request):
    form = forms.rentalform(request.POST)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect(indexview)
    else:
        print(form.errors)
    return render(request,'rentals/forms.html')



def r_loginview(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect(formsview)
        else:
            return HttpResponse("user not found")
    return render(request,'rentals/login.html')

def r_logoutview(request):
    logout(request)
    return redirect(indexview)


def r_registerview(request):
        if request.method == 'POST':
            if request.POST.get('password') == request.POST.get('password1'):
                try:
                    User.objects.get(username=request.POST.get('username'))
                    messages.error(request,"Username already in use")
                except:
                    User.objects.create_user(username=request.POST.get('username'),
                                         password=request.POST.get('password'))
                    messages.success(request,"User registered Successfully")
                    return redirect(r_loginview)
            else:
                messages.error(request,"Passwords do not match")
                print("errror")
        return render(request,'rentals/register.html')

