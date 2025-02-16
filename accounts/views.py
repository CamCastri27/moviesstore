from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import CustomUserCreationForm, CustomErrorList
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth import login
@login_required
def orders(request):
    template_data = {}
    template_data['title'] = 'Orders'
    template_data['orders'] = request.user.order_set.all()
    return render(request, 'accounts/orders.html',
        {'template_data': template_data})
@login_required
def logout(request):
    auth_logout(request)
    return redirect('home.index')


def login(request):
    template_data = {}
    template_data['title'] = 'Login'

    if request.method == 'GET':
        return render(request, 'accounts/login.html', {'template_data': template_data})

    elif request.method == 'POST':
        # Get the username or email from the POST data
        username_or_email = request.POST['username']
        password = request.POST['password']

        # Check if the input is an email address
        if '@' in username_or_email:
            try:
                # If it's an email, get the user by email and use their username for authentication
                user = User.objects.get(email=username_or_email)
                username = user.username
            except User.DoesNotExist:
                user = None
        else:
            # Otherwise, it's a username
            username = username_or_email
            user = User.objects.filter(username=username).first()

        # Authenticate the user
        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(request, 'accounts/login.html', {'template_data': template_data})

        # Authenticate with the username and password
        user = authenticate(request, username=username, password=password)

        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(request, 'accounts/login.html', {'template_data': template_data})

        # Log the user in
        auth_login(request, user)
        return redirect('home.index')



def signup(request):
    template_data = {'title': 'Sign Up'}
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {'template_data': template_data})

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)# Saves the user with email, username, and password
            return redirect('home.index')  # Redirect after successful sign-up
        else:
            template_data['form'] = form  # Pass the form with errors back to the template
    else:
        form = CustomUserCreationForm()  # Display empty form for GET requests
        template_data['form'] = form

    return render(request, 'accounts/signup.html', {'template_data': template_data})


# Create your views here.