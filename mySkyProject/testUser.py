
import os
import django
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mySkyProject.settings')
django.setup()

User = get_user_model()

def create_test_user():
    try:
        test_user = User.objects.create(
            user_id='test_Skyuser_id',
            name='Test Sky user',
            email='test@sky.com',
            password=make_password('testPass01.'),  # Hardcoded password
            role='test_role',
            is_staff=True,
            is_superuser=True
        )
        print(f"Test user created with email: {test_user.email} and password: testPass01.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    create_test_user()