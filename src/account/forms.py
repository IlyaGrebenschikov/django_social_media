from typing import Any
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from .models import CustomUser


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='username', initial='')
    email = forms.EmailField(label='email', initial='')
    password1 = forms.CharField(label='password1', initial='', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2', initial='', widget=forms.PasswordInput)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


class SignInForm(AuthenticationForm):
    username = forms.CharField(label='Name', initial='')
    password = forms.CharField(label='Password', initial='', widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ('username', 'password')
