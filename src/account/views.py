from typing import Any

from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.forms import ValidationError
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http.response import HttpResponse
from django.urls import reverse_lazy

from .forms import SignUpForm, SignInForm
from .models import CustomUser


class UserSignUpView(CreateView):
    template_name = 'account/sign_up.html'
    form_class = SignUpForm
    
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

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        if 'password2' in form.errors:
            messages.error(self.request, "Passwords dont match")
            
        return super().form_invalid(form)
    
    def get_success_url(self) -> str:
        return reverse_lazy('user_detail', kwargs={'pk': self.request.user.pk})


class UserSignInView(LoginView):
    form_class = SignInForm
    model = CustomUser
    template_name = 'account/sign_in.html'
    redirect_authenticated_user = True
    
    def get_success_url(self) -> str:
        return reverse_lazy('user_detail', kwargs={'pk': self.request.user.pk})
    
    def form_invalid(self, form) -> HttpResponse:
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home_page')


class UserDetailView(DetailView, LoginRequiredMixin):
    model = CustomUser
    template_name = 'account/details.html'
    context_object_name = 'user'
    http_method_names = ['get']
    
    def get_queryset(self) -> QuerySet[Any]:
        current_user = self.request.user
        queryset = super().get_queryset()
        
        return queryset.filter(pk=current_user.pk)   
