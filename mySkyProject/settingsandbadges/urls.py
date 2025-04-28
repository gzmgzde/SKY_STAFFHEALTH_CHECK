from django.urls import path
from . import views 


urlpatterns = [
    path('', views.settingPage, name="settings"),
    path('badges/', views.badgesPage, name="badges")
]