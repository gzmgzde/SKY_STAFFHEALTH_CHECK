"""
Definition of models.
"""

from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.email  # Assuming you want to display the user's email