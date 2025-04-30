
from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name="welcomePage_home"),
    path('login/', views.login, name="welcomePage_login"),
    path('forgot_password/', views.forgot_password, name="welcomePage_forgot_password"),
    path('password_reset/', views.password_reset, name="welcomePage_password_reset"),
    path('register/', views.register, name="welcomePage_register"),
]
