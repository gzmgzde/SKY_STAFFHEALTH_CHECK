from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate



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
    return render(request, 'forgot_password.html')


def password_reset(request):
    return render(request, 'password_reset.html')


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

