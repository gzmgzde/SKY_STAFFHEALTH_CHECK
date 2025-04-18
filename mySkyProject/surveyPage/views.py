from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def survey(request):
    return render(request, 'surveyQ1.html')
def survey_q2(request):
    return render(request, 'surveyQ2.html')
def survey_q3(request):
    return render(request, 'surveyQ3.html')
def survey_q4(request):
    return render(request, 'surveyQ4.html')
def survey_q5(request):
    return render(request, 'surveyQ5.html')
def survey_q6(request):
    return render(request, 'surveyQ6.html')
def survey_q7(request):
    return render(request, 'surveyQ7.html')
def survey_q8(request):
    return render(request, 'surveyQ8.html')
def survey_q9(request):
    return render(request, 'surveyQ9.html')
def survey_q10(request):
    return render(request, 'surveyQ10.html')
def survey_q11(request):
    return render(request, 'surveyQ11.html')
def survey_q12(request):
    return render(request, 'surveyQ12.html')
def survey_q13(request):
    return render(request, 'surveyQ13.html')
def survey_q14(request):
    return render(request, 'surveyQ14.html')