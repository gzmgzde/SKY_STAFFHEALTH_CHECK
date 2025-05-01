from django.urls import path
from . import views 



urlpatterns = [
    path('', views.survey, name='survey'),
    path('question/<int:question_number>/', views.survey_question, name='survey_question'),
]