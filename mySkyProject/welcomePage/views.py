from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from mySkyProject import settings
from .models import User
from .forms import ForgotPasswordForm, PasswordResetForm, UserRegisterForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail



# Create your views here.

def home(request):
    return render(request, 'homePage.html')


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)  # Log the user in
                return redirect('/dashboard')  # Redirect to the dashboard page after successful login
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})


def forgot_password(request):
    User = get_user_model()
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
            # Check if user exists in the database
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                form.add_error('email', 'This email is not registered.')
                return render(request, 'forgot_password.html', {'form': form})

            # Generate token for password reset
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(str(user.pk).encode())

            # Create the reset link
            reset_link = request.build_absolute_uri(
                f"/reset_password/{uid}/{token}/"
            )

            # Send reset link to the user
            subject = 'Password Reset Request'
            message = render_to_string(
                'password_reset.html',
                {
                    'user': user,
                    'reset_link': reset_link,
                }
            )
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

            return redirect('/password_reset')  
    else:
        form = ForgotPasswordForm()

    return render(request, 'forgot_password.html', {'form': form})


def password_reset(request):
        if request.method == 'POST':
            form = ForgotPasswordForm(request.POST)
            if form.is_valid():
                # Set and save the new password
                new_password = form.cleaned_data['password']
                User.set_password(new_password)
                User.save()

                messages.success(request, 'Your password has been reset successfully.')
            return redirect('login')  # Redirect to login page after successful password reset
        else:
            form = PasswordResetForm()
        return render(request, 'password_reset.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            messages.success(request, f'Your account was created successfully')

            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')

