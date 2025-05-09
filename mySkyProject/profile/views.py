"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def profile(request):
    # Your view logic here
    return render(request, 'profile/profile.html')