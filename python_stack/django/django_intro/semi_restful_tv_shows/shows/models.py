from django.db import models
from django.utils import timezone
from datetime import date
from datetime import datetime


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        # Allow empty description but if its not empty it needs to have at least 10 characters
        if len(postData['description']) > 0 and len(postData['description']) < 10:
            errors["description"] = "Show description can be empty, otherwise it needs to be at least 10 characters"

        if len(postData['release_date']) > 0:
            if datetime.strptime(postData['release_date'], "%Y-%m-%d") > datetime.today():
                errors["release_date"] = "Show release date cannot be in the future"
        else:
            errors["release_date"] = "Show release date cannot be blank"

        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
