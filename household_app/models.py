from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class rental(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.EmailField(max_length=120)

class product_rent(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    productType = models.CharField(max_length=100)
    boughtdate = models.DateField()
    image = models.ImageField(upload_to='pro_image')
    price = models.FloatField()
