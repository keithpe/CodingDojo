from django.db import models
import datetime

# Import the user model from the login app
from login.models import User


class AuthorManager(models.Manager):

    def basic_validator(self, postData):

        errors = {}

        if len(postData['first_name']) == 0:
            errors['first_name'] = 'Author first name cannot be empty'

        if len(postData['last_name']) == 0:
            errors['last_name'] = 'Author last name cannot be empty'

        return errors


class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()


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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        Author, related_name="books_written", on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name="books_uploaded", on_delete=models.CASCADE)
    objects = BookManager()


class Review(models.Model):
    text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, related_name="books_reviewed_by", on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book, related_name="reviews_for_this_book", on_delete=models.CASCADE)
