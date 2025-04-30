from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from surveyPage.models import User
from django.views.decorators.http import require_POST

# Create your views here.
def settingPage(request):
    return render(request, 'settingPage.html')

def logout_view(request):
    # Clear all session data
    request.session.flush()
    # Redirect to home page
    return redirect('/')

@require_POST
def change_password(request):
    try:
        current_password = request.POST.get('currentPassword')
        new_password = request.POST.get('newPassword')
        user_id = '001'  # Using static user_id for now
        
        # Get the user
        user = User.objects.get(user_id=user_id)
        
        # Check if current password matches
        if user.password != current_password:
            return JsonResponse({
                'status': 'error',
                'message': 'Current password is incorrect'
            }, status=400)
        
        # Update the password
        user.password = new_password
        user.save()
        
        return JsonResponse({
            'status': 'success',
            'message': 'Password updated successfully'
        })
        
    except User.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'User not found'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)