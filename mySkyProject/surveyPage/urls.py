from django.urls import path
from . import views 


urlpatterns = [
    path('', views.survey, name="survey"),
    path('survey/q2/', views.survey_q2, name='survey_q2'),
    path('survey/q3/', views.survey_q3, name='survey_q3'),
    path('survey/q4/', views.survey_q4, name='survey_q4'),
    path('survey/q5/', views.survey_q5, name='survey_q5'),
    path('survey/q6/', views.survey_q6, name='survey_q6'),
    path('survey/q7/', views.survey_q7, name='survey_q7'),
    path('survey/q8/', views.survey_q8, name='survey_q8'),
    path('survey/q9/', views.survey_q9, name='survey_q9'),
    path('survey/q10/', views.survey_q10, name='survey_q10'),
    path('survey/q11/', views.survey_q11, name='survey_q11'),
    path('survey/q12/', views.survey_q12, name='survey_q12'),
    path('survey/q13/', views.survey_q13, name='survey_q13'),
    path('survey/q14/', views.survey_q14, name='survey_q14'),
]