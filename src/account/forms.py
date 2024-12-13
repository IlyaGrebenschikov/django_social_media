from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from .models import CustomUser


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Name', initial='')
    email = forms.EmailField(label='email', initial='')

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class SignInForm(AuthenticationForm):
    username = forms.CharField(label='Name', initial='')
    password = forms.CharField(label='Password', initial='', widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ('username', 'password')
