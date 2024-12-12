from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import CustomUser


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Name')
    email = forms.EmailField(label='email')

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
        