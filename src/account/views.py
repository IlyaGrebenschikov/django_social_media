from typing import Any

from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http.response import HttpResponse
from django.urls import reverse_lazy

from .forms import SignUpForm
from .models import CustomUser


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


class UserSignInView(LoginView):
    model = CustomUser
    template_name = 'account/sign_in.html'
    redirect_authenticated_user = True
    
    def get_success_url(self) -> Any:
        return reverse_lazy('home_page')
    
    def form_invalid(self, form) -> HttpResponse:
        messages.error(self.request, 'Invalid username or password.')
        
        return super().form_invalid(form)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home_page')
    