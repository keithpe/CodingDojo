from django.db import models
from django.utils import timezone
from datetime import date
from datetime import datetime


class CourseManager(models.Manager):
    def basic_validator(self, postData):

        errors = {}

        if len(postData['name']) < 6:
            errors['name'] = 'Name must be more than 5 characters'
        if len(postData['description']) < 16:
            errors['description'] = 'Description must be more than 15 characters'
        return errors


class Description(models.Model):

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Course(models.Model):

    name = models.CharField(max_length=255)
    description = models.OneToOneField(
        Description, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
