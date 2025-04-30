from django.urls import path
from . import views 

app_name = 'settingsandbadges'  # Namespace for the app

urlpatterns = [
    path('', views.settingPage, name="settings"),
    path('badges/', views.badgesPage, name="badges")
]