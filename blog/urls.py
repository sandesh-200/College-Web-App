from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
    path('notice/', views.notice, name='blog-notice'),
    path('handleReg/', views.handleReg, name='blog-reg'),
    path('handleLogin/', views.handleLogin, name='blog-login'),
    path('handlelogout/', views.handlelogout, name='blog-logout'),
    path('user_profile/', views.user_profile, name="blog-user_profile")
]