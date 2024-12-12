from typing import Any

from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponse

from .forms import SignUpForm


class UserSignUpView(CreateView):
    template_name = 'account/sign_up.html'
    form_class = SignUpForm
    success_url = '/'

    def form_valid(self, form) -> HttpResponse:
        response = super().form_valid(form) 
        user = authenticate(
            self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
            )
        
        if user:
            login(self.request, user) 
        
        return response
    