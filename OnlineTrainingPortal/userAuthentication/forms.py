
from cProfile import label
from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


# # Modify Registration Form
# class SignUpForm(UserCreationForm):
#     password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
#     class Meta:
#         model = User
#         fields = ['first_name','last_name','username','email']
#         labels = {'first_name':'First Name','last_name':'Last Name', 'email':'email'}


class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm,self).__init__(*args,**kwargs)
        for fieldname in ['username','password1','password2']:
            self.fields[fieldname].help_text = None
            
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        user.is_approved = False
        if commit:
            user.save()
        return user

class StudentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm,self).__init__(*args,**kwargs)
        for fieldname in ['username','password1','password2']:
            self.fields[fieldname].help_text = None
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        user.is_approved = True
        if commit:
            user.save()
        return user

class AdminSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name','last_name','username','email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        # user.approval= False
        if commit:
            user.save()
        return user

class AdminSiteUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name','last_name','username','email','password1','password2','is_student','is_teacher','is_admin','is_approved']
        
    def save(self, commit=True):
        user = super().save(commit=False)