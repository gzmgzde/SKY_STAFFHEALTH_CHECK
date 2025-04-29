from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
]