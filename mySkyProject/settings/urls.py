from django.urls import path
from . import views 


urlpatterns = [
    path('', views.settingPage, name="settings"),
    path('logout/', views.logout_view, name="logout"),
    path('change-password/', views.change_password, name="change_password"),
]