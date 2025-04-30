from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Department, User, Team
import uuid
import logging
from django.db import transaction

logger = logging.getLogger(__name__)

class UserRegisterForm(UserCreationForm):
    ROLE_CHOICES = [
        ('', 'Select Role'),
        ('Senior Engineer', 'Senior Engineer'),
        ('Team Leader', 'Team Leader'),
        ('Department Leader', 'Department Leader'),
        ('Engineer', 'Engineer'),
    ]

    email = forms.EmailField(
        required=True,
        help_text="Enter a valid email address.",
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
    )
    name = forms.CharField(
        max_length=100,
        required=True,
        label="Name",
        help_text="Enter your full name.",
        widget=forms.TextInput(attrs={'placeholder': 'Full Name'}),
    )
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True,
        label="Role",
        help_text="Select your role.",
    )
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        empty_label="Select Department",
        required=True,
        label="Department",
        help_text="Select your department.",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    team = forms.ModelChoiceField(
        queryset=Team.objects.all(),
        empty_label="Select Team",
        required=True,
        label="Team",
        help_text="Select your team.",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    terms_conditions = forms.BooleanField(
        required=True,
        label="I accept the Terms and Conditions",
        error_messages={'required': 'You must accept the Terms and Conditions to register.'},
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        help_text="Enter a strong password.",
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        help_text="Re-enter your password for confirmation.",
    )

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'name', 'role', 'department', 'team', 'terms_conditions']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def save(self, commit=True):
        try:
            logger.debug("Starting form.save()")
            with transaction.atomic():
                user = super().save(commit=False)
                user.email = self.cleaned_data['email']
                user.name = self.cleaned_data['name']
                user.role = self.cleaned_data['role']
                user.username = self.cleaned_data['email']
                user.set_password(self.cleaned_data['password1'])
                user.user_id = str(uuid.uuid4())

                # Department and team are already model instances thanks to ModelChoiceField
                # so we can assign them directly
                user.department = self.cleaned_data['department']
                user.team = self.cleaned_data['team']
                
                logger.debug(f"Department: {user.department}")
                logger.debug(f"Team: {user.team}")

                if commit:
                    logger.debug("Saving user to database")
                    user.save()
                    logger.debug(f"User saved: {user.email} with ID: {user.user_id}")
                
                return user
                
        except Exception as e:
            logger.error(f"An error occurred while saving the user: {e}")
            raise



class UserLoginForm(AuthenticationForm):
    # Override the default username field to use EmailField
        username = forms.EmailField(
            widget=forms.EmailInput(attrs={
                'placeholder': 'Email'
            }),
            label="Email"  # You can define label here as well
        )

        password = forms.CharField(
            widget=forms.PasswordInput(attrs={
                'placeholder': 'Password'
            }),
            label="Password"
        )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Although we already set the labels in field declaration,
            # this reinforces that 'username' should be labelled as "Email"
            self.fields['username'].label = "Email"
            self.fields['password'].label = "Password"

        def clean(self):
            # Call the base class clean method to run the standard authentication logic.
            cleaned_data = super().clean()
            if not cleaned_data.get('username'):
                raise forms.ValidationError("Email is required.")
            if not cleaned_data.get('password'):
                raise forms.ValidationError("Password is required.")
            return cleaned_data

        def clean_username(self):
            username = self.cleaned_data.get('username')
            # Check if the user exists for a given email.
            if username and not User.objects.filter(email=username).exists():
                raise forms.ValidationError("This email is not registered.")
            return username

        def clean_password(self):
            password = self.cleaned_data.get('password')
            if not password:
                raise forms.ValidationError("Password is required.")
            return password