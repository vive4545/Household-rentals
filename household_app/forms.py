from django import forms
from household_app import models
from django.contrib.auth.models import User

class rentalform(forms.ModelForm):
    class Meta:
        model = models.rental
        fields = "__all__"
        exclude =('user',)

class product_rentform(forms.ModelForm):
    class Meta:
        model = models.product_rent
        fields = "__all__"
        exclude =('user',)