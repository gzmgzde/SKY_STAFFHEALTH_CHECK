from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Department, User, Team
import uuid
import logging
from django.db import transaction

logger = logging.getLogger(__name__)

class UserRegisterForm(UserCreationForm):
    # Define the choices for the role field
    ROLE_CHOICES = [
        ('', 'Select Role'),
        ('Senior Engineer', 'Senior Engineer'),
        ('Team Leader', 'Team Leader'),
        ('Department Leader', 'Department Leader'),
        ('Engineer', 'Engineer'),
    ]

    # Define the form fields
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

    # Define the department and team fields
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
    # Password fields
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
    # Meta class to link the form to the User model
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'name', 'role', 'department', 'team', 'terms_conditions']

#     # Customizing the widgets for better UI
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
                # Create a new user instance but don't save it yet
                user = super().save(commit=False)
                user.email = self.cleaned_data['email']
                user.name = self.cleaned_data['name']
                user.role = self.cleaned_data['role']
                user.username = self.cleaned_data['email']
                user.set_password(self.cleaned_data['password1'])
                # Generate a unique user ID
                user.user_id = str(uuid.uuid4())

                # Department and team assigning 
                user.department = self.cleaned_data['department']
                user.team = self.cleaned_data['team']
                
                # Log the user details for debugging
                logger.debug(f"Department: {user.department}")
                logger.debug(f"Team: {user.team}")

                # Savve the user instance to the database if commit is True
                if commit:
                    logger.debug("Saving user to database")
                    user.save()
                    logger.debug(f"User saved: {user.email} with ID: {user.user_id}")
                
                return user
            
        # Handle any exceptions that occur during the save process
        except Exception as e:
            logger.error(f"An error occurred while saving the user: {e}")
            raise


# Custom form for user login
class UserLoginForm(AuthenticationForm):
        
    # Override the default username field to use EmailField
        username = forms.EmailField(
            widget=forms.EmailInput(attrs={
                'placeholder': 'Email'
            }),
            label="Email" 
        )

        password = forms.CharField(
            widget=forms.PasswordInput(attrs={
                'placeholder': 'Password'
            }),
            label="Password"
        )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            
            self.fields['username'].label = "Email"     # Change label to "Email"
            self.fields['password'].label = "Password"

        def clean(self):
            # Call the base class clean method to run the standard authentication logic.
            cleaned_data = super().clean()
            if not cleaned_data.get('username'):
                raise forms.ValidationError("username is required.")
            if not cleaned_data.get('password'):
                raise forms.ValidationError("Password is required.")
            return cleaned_data

        # Custom validation for the username field
        def clean_username(self):
            username = self.cleaned_data.get('username')
            # Check if the user exists for a given email.
            if username and not User.objects.filter(email=username).exists():
                raise forms.ValidationError("This email is not registered.")
            return username

# Custom validation for the password field
        def clean_password(self):
            password = self.cleaned_data.get('password')
            if not password:
                raise forms.ValidationError("Password is required.")
            return password
        

# Custom form for password reset
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        required=True,
        help_text="Enter your registered email address.",
        widget=forms.EmailInput(attrs={'placeholder': 'Email' ,'style': 'color: white;'})

    )
     # Custom validation for the email field
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is not registered.")
        return email
    
# Custom form for password reset confirmation
class PasswordResetForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter new Password'}), label="New Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm new Password'}), label="Confirm Password")
    
    # Custom validation for the new password and confirm password fields
    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password != confirm_password:
            raise forms.ValidationError("The two password fields must match.")

        return cleaned_data