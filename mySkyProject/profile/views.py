"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    return render(request, 'profile/profile.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  # Redirect to a success page.
        else:
            return render(request, 'welcomePage/login.html', {'error': 'Invalid email or password'})
    return render(request, 'welcomePage/login.html')