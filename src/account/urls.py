from django.urls import path

from . import views


urlpatterns = [
    path('sign_up/', views.UserSignUpView.as_view(), name='sign_up'),
    path('sign_in/', views.UserSignInView.as_view(), name='sign_in'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]
