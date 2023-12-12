from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'block border border-grey-light w-full p-3 rounded mb-4','placeholder':'Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'block border border-grey-light w-full p-3 rounded mb-4','placeholder':'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'block border border-grey-light w-full p-3 rounded mb-4','placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'block border border-grey-light w-full p-3 rounded mb-4','placeholder':'Confirm-Password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


