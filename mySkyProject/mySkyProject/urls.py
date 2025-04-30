"""
URL configuration for mySkyProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from welcomePage import views as welcome_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('welcomePage.urls')),
    path('survey/', include('surveyPage.urls')),
    path('settings/', include('settings.urls')),
    path('badges/', include('badges.urls')),
    path('profile/', include('pageProfile.urls')),
    path('dashboard/', include('dashboardPage.urls')),

    path('forgot-password/', welcome_views.forgot_password, name='forgot_password'),
    path('login/', welcome_views.login_view, name='login'),
    path('register/', welcome_views.register, name='register'),
    path('create-new-password/', welcome_views.password_reset, name='create_new_password'),

]
