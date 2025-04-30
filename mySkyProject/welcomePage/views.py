from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'homePage.html')


def login(request):
    return render(request, 'login.html')


def forgot_password(request):
    return render(request, 'forgot_password.html')


def password_reset(request):
    return render(request, 'password_reset.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            messages.success(request, f'Your account was created successfully')

            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')