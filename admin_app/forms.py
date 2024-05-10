from django import forms
from admin_app import models
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

from client_app.models import clientdetails

class customerform(forms.ModelForm):
    class Meta:
        model = models.customer
        fields = "__all__"
        exclude =('user',)

class clientforms(forms.ModelForm):
    class Meta:
        model = clientdetails
        fields = "__all__"
        exclude =('user',)

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Old Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

class CouponForm(forms.ModelForm):
    class Meta:
        model = models.Coupon
        fields = "__all__"
        exclude = ('user',)
