from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def survey(request):
    return render(request, 'surveyQ1.html')