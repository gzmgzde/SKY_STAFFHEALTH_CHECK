from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('', views.profilePage, name='profile'),
]