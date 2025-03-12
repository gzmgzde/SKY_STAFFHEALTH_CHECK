
from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name="welcomePage_home"),
]
