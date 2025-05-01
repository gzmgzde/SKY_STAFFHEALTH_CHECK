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
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('welcomePage.urls')),
    path('survey/', include('surveyPage.urls')),
    path('settings/', include('settings.urls')),
    path('badges/', include('badges.urls')),
    path('profile/', include('pageProfile.urls')),
    path('dashboard/', include('dashboardPage.urls')),


    #please dont delete this.
    path('login/', auth_views.LoginView.as_view(template_name='welcomePage/login.html'), name='login'),
     path('forgot_password/', auth_views.PasswordChangeView.as_view(template_name='welcomePage/forgot_password.html'), name='forgot_password'),
     path('password_reset/', auth_views.PasswordChangeDoneView.as_view(template_name='welcomePage/password_reset.html'), name='password_reset'),
     path('register/', auth_views.PasswordResetView.as_view(template_name='welcomePage/register.html'), name='register'),
 ]

