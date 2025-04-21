from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def survey(request):
    return render(request, 'surveyQ1.html', {'current_question': 1})
def survey_q2(request):
    return render(request, 'surveyQ2.html', {'current_question': 2})
def survey_q3(request):
    return render(request, 'surveyQ3.html', {'current_question': 3})
def survey_q4(request):
    return render(request, 'surveyQ4.html', {'current_question': 4})
def survey_q5(request):
    return render(request, 'surveyQ5.html', {'current_question': 5})
def survey_q6(request):
    return render(request, 'surveyQ6.html', {'current_question': 6})
def survey_q7(request):
    return render(request, 'surveyQ7.html', {'current_question': 7})
def survey_q8(request):
    return render(request, 'surveyQ8.html', {'current_question': 8})
def survey_q9(request):
    return render(request, 'surveyQ9.html', {'current_question': 9})
def survey_q10(request):
    return render(request, 'surveyQ10.html', {'current_question': 10})
def survey_q11(request):
    return render(request, 'surveyQ11.html', {'current_question': 11})
def survey_q12(request):
    return render(request, 'surveyQ12.html', {'current_question': 12})
def survey_q13(request):
    return render(request, 'surveyQ13.html', {'current_question': 13})
def survey_q14(request):
    return render(request, 'surveyQ14.html', {'current_question': 14})