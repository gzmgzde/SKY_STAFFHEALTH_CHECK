from django.urls import path
from . import views 

app_name = 'dashboard'  # Namespace for the app

urlpatterns = [
    path('', views.dashboard, name="dashboardPage"),
]
