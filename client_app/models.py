from django.db import models
from django.contrib.auth.models import User
from household_app.models import product_rent
# Create your models here.
class clientdetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.EmailField(max_length=120)
    address=models.CharField(max_length=100)
    proof = models.ImageField(upload_to='pro_image')

class contactdetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=120)
    phone = models.BigIntegerField()
    subject = models.CharField(max_length=300)
    message = models.CharField(max_length=200)

class customerproduct(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.BigIntegerField()
    productimage = models.ImageField(upload_to='productimage')
    quantity = models.IntegerField()

class FinalOrder(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    total = models.BigIntegerField()

class ConfirmOrder(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    final = models.ForeignKey(FinalOrder,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(product_rent,on_delete=models.CASCADE)
    quantity = models.FloatField()
    subtotal = models.BigIntegerField()

class billingproduct(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    final = models.ForeignKey(FinalOrder,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.BigIntegerField()


