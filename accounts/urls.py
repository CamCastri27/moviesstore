from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import forgot_password




urlpatterns = [
    path('signup', views.signup, name='accounts.signup'),
    path('login/', views.login, name='accounts.login'),
    path('logout/', views.logout, name='accounts.logout'),
    path('orders/', views.orders, name='accounts.orders'),
    path('forgot-password/', forgot_password, name='forgot_password'),





]