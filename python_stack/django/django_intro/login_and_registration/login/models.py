from django.db import models
import re


class UserManager(models.Manager):
    def basic_validator(self, postData):

        errors = {}

        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First Name must be at least 2 characters'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last Name must be at least 2 characters'
        if len(postData['password']) < 8:
            errors['password_length'] = 'Password must be at least 8 characters'
        if postData['password'] != postData['confirm_pw']:
            errors['password_confirm'] = 'Password and confirm values are different'
        if len(postData['email']) < 8:
            errors['email_length'] = 'Email cannot be empty'

        # Check for invalid email
        pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        result = re.match(pattern, postData['email'])
        if not result:
            errors['email'] = 'Invalid email address'

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
