from django.urls import path

from . import views


urlpatterns = [
    path('sign_in/', views.UserSignUpView.as_view(), name='sign_in'),
]
