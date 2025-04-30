from django.shortcuts import render, redirect
from django.http import HttpResponse
from surveyPage.models import Vote, User

# Create your views here.
def badges(request):
    # Use static user_id
    static_user_id = '001'
    
    try:
        # Get all votes for the static user
        user_votes = Vote.objects.filter(user__user_id=static_user_id)
        
        # Calculate total votes
        total_votes = user_votes.count()
        
        # Determine badge level based on vote count
        if total_votes >= 9:
            badge_level = 9
        elif total_votes >= 8:
            badge_level = 8
        elif total_votes >= 7:
            badge_level = 7
        elif total_votes >= 6:
            badge_level = 6
        elif total_votes >= 5:
            badge_level = 5
        elif total_votes >= 4:
            badge_level = 4
        elif total_votes >= 3:
            badge_level = 3
        elif total_votes >= 2:
            badge_level = 2
        elif total_votes >= 1:
            badge_level = 1
        else:
            badge_level = 0
            
    except Exception as e:
        # Handle any errors
        badge_level = 0
        total_votes = 0
        user_votes = []
    
    return render(request, 'badgesPage.html', {
        'badge_level': badge_level,
        'total_votes': total_votes
    })

def logout_view(request):
    # Clear all session data
    request.session.flush()
    # Redirect to home page
    return redirect('/')

