from django import forms
from . models import studentform
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField


class student(forms.ModelForm):
    class Meta:
        model=studentform
        fields=["name","email","password"]
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(render_value=True,attrs={"class":"form-control"}),  
        }
        
class signform(UserCreationForm):
    password1=forms.CharField(label="password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(label="confirm password",widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta(UserCreationForm):
        model=User
        fields=["username","first_name","last_name","email"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),  
        }
        
class loginform(AuthenticationForm):
        username=UsernameField(widget=forms.TextInput(attrs={"class":"form-control"}))
        password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))