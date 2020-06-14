from django.db import models
import datetime

# Import the user model from the login app
from login.models import User


class BookManager(models.Manager):
    def basic_validator(self, postData):

        errors = {}

        if len(postData['title']) == 0:
            errors['title'] = 'Title cannot be empty'

        if len(postData['description']) < 5:
            errors['description'] = 'Description must be at least 5 characters'

        return errors


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    objects = BookManager()
