from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.EmailField(max_length=120)
    address=models.CharField(max_length=100)
    phone=models.BigIntegerField()

    
class client_model(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=120)
    address = models.CharField(max_length=100)
    proof = models.ImageField(upload_to='proof_image')

class Coupon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    discount = models.TextField(max_length=1000)
    expiry_date = models.DateTimeField()
