from django.db import models

# Import the user model from the login app
from login.models import User


class AuthorManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['name']) == 0:
            errors['name'] = 'Author name cannot be empty'

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
