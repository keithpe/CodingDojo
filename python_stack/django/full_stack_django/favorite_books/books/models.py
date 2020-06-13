from django.db import models
import datetime

# Import the user model from the login app
from login.models import User


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, related_name="books", on_delete=models.CASCADE)
    favorites = models.ManyToManyField(User)
