from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class Sign_Up_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        
        
        
class user_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name' )        
        
        
        
class profile_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number', 'adress', )        