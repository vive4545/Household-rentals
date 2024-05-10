from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from client_app import forms
from client_app import models
from django.urls import path
from household_app.models import product_rent
from admin_app.models import Coupon
from . import views
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage ,PageNotAnInteger



# Create your views here.


#<----------------(Index and about)--------------------->



def clientindexview(request):
    data = product_rent.objects.all()
    return render(request,'clients/index.html',{'data':data})


def c_aboutview(request):
    return render(request,'clients/about.html')





# <------------------------(details,shop single product ,contact and purchase )----------------------->





def c_detailsview(request):
    if request.method == "POST":
        form = forms.customerform(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            print(obj)
            return redirect(clientindexview)
        else:
            print(form.errors)
    return render(request,'clients/clientdetails.html')


def clientshop(request):
    data =product_rent.objects.all()
    context = {'data':data}
    return render(request,'clients/shop.html',context=context)



def c_contactview(request):
    if request.method == 'POST':
        form = forms.contactForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            print(obj)
            return redirect(c_contactview)
        else:
            print(form.errors)
    return render(request,'clients/contact.html')



def c_singleview(request):
    return render(request,'clients/single-product.html')






# <-------------------(Login log out and register)-------------------------------->



def c_loginview(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect(c_detailsview)
        else:
            return render(c_errorview)
    return render(request,'clients/login.html')



def c_registerview(request):
        if request.method == 'POST':
            if request.POST.get('password') == request.POST.get('password1'):
                try:
                    User.objects.get(username=request.POST.get('username'))
                    return HttpResponse("username already exist")
                except:
                    User.objects.create_user(username=request.POST.get('username'),
                                             password=request.POST.get('password'),
                                             email=request.POST.get('email')),
                    
                    return redirect(c_loginview)
        return render(request,'clients/register.html')


def c_logoutview(request):
    logout(request)
    return redirect(c_loginview)



#<-------------------------(cart details,add,edit,)---------------------->



def cart_add(request, id):
    cart = Cart(request)
    product = product_rent.objects.get(id=id)
    cart.add(product=product)
    return redirect(c_cartview)



def cart_edit(request,id):
    cart = Cart(request)
    product = product_rent.objects.get(id=id)
    cart.edit(product=product)
    return redirect(clientindexview)




def c_cartview(request):
    cart = Cart(request)
    data = models.customerproduct.objects.all()
    subtotal = 0
    for  ab in cart.cart.values():
        subtotal += float(ab['price']) * float(ab['quantity'])    
    print("subtotal is ",subtotal)  
    gst = 0.18 * subtotal 
    total = gst + subtotal    
    context = {
        'data':data,
        'total': total,
        'subtotal': subtotal,
        'gst': gst,
        }
    return render(request, 'clients/cart.html',context=context)





def c_errorview(request):
    return render(request,'clients/404.html')

# <----------------CHECHKOUT ---------------->

@login_required(login_url="/users/login")
def c_checkoutview(request,id):
    cart = Cart(request)
    subtotal = 0
    num = 0
    coupan  = id

    x = cart.cart.values()
    print(x)
    y = list(x)
    print(y)
    prod_ids = [item['product_id'] for item in y]
    print(prod_ids)

    fnl = models.FinalOrder.objects.create(user=request.user,total=0)

    for item in cart.cart.values():
        price = float(item['price'])
        quantity = float(item['quantity'])
        sub = price * quantity
        subtotal += price * quantity
        prod = models.product_rent.objects.get(id=prod_ids[num])
        print(prod)
        order = models.ConfirmOrder.objects.create(user=request.user,
                                                   subtotal = sub,
                                                   quantity = quantity,
                                                   final = fnl,
                                                   product =prod)
        num+=num+1

    

    gst = 0.18 * subtotal
    total = subtotal + gst
    total_last = total - coupan
    
    fnl.total = total
    fnl.save()
    
    if request.method == 'POST':
        form = forms.billingform(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.final = fnl
            obj.save()
            print(obj)
            return redirect(payments)
        else:
            print(form.errors)


    context = {
        'subtotal': subtotal,
        'gst': gst,
        'total': total,
        'coupan':coupan,
        'total_last':total_last,
    }
    return render(request, 'clients/checkout.html',context)



# <--------------------------------------------------------------->
def item_increment(request, id):
    cart = Cart(request)
    product = product_rent.objects.get(id=id)
    cart.add(product=product)
    return redirect(c_cartview)




def item_decrement(request, id):
    cart = Cart(request)
    product = product_rent.objects.get(id=id)
    cart.decrement(product=product)
    return redirect(c_cartview)




def item_clear(request, id):
    cart = Cart(request)
    product = product_rent.objects.get(id=id)
    cart.remove(product)
    return redirect(c_cartview)


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect(c_cartview)


@login_required(login_url="/users/login")
def payments(request):
    return render(request, 'clients/payment.html')


def searchview(request):
    if request.method == 'POST':
        data =product_rent.objects.all()
        search = request.POST.get('search')
        srch_data = product_rent.objects.filter(name__icontains=search)
        print("searched data",srch_data)
        context = {'data':srch_data}
    return render(request,'clients/shop.html',context)


import random
from django.core.mail import send_mail
from django.conf import settings


def forget_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        code = random.randint(100000, 999999)  
        print("password", code)
        user = User.objects.get(email=email)
        print(user)
        subject = "Forget password"
        msg = f"Your new password for {user} is {code}."  
        from_email = settings.EMAIL_HOST_USER
        receipent = [email]

        user.set_password(str(code))
        user.save()

        send_mail(subject, msg, from_email, receipent)
        print("mail sent ......................")
        return redirect(c_loginview)
    
    return render(request, 'clients/forgetpassword.html')


@login_required(login_url="/users/login")
def applycoupan(request):
    if request.method == "POST":
        coupan = request.POST.get('coupan')
        print(coupan)
        chck = Coupon.objects.get(code=coupan)
        print("checkkkkkkkk",chck)
        print("checkkkkkkkk",chck.discount)
        return redirect(c_checkoutview,chck.discount)