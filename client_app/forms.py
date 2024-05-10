from django import forms
from client_app import models
from django.contrib.auth.models import User

class customerform(forms.ModelForm):
    class Meta:
        model = models.clientdetails
        fields = "__all__"
        exclude =('user',)

class contactForm(forms.ModelForm):
    class Meta:
        model = models.contactdetails
        fields = "__all__"
        exclude =('user',)

class productForm(forms.ModelForm):
    class Meta:
        model = models.customerproduct
        fields = "__all__"
        exclude =('user',)
class billingform(forms.ModelForm):
    class Meta:
        model = models.billingproduct
        fields = "__all__"
        exclude =('user','final')
