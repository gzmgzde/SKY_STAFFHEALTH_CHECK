from django.shortcuts import render

# Create your views here.
def settingPage(request):
    return render(request, 'settingPage.html')

def badgesPage(request):
    badge_level = 2
    return render(request, 'badgesPage.html', {'badge_level': badge_level})