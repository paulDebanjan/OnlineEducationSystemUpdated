from cProfile import label
from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class login(forms.Form):
    user = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class': 'form-control'}))
    pas = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))




# class calculate(forms.Form):
#     value1 = forms.CharField(label='Value 1', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     operator = forms.ChoiceField()
#     value2 = forms.CharField(label='Value 2', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))


class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']