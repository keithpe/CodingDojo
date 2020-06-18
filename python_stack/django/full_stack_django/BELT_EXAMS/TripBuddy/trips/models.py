from django.db import models

# Import the user model from the login app
from login.models import User
import datetime


class TripManager(models.Manager):

    def basic_validator(self, postData):

        errors = {}

        # Check length of destination and plan fields
        if len(postData['destination']) < 3:
            errors['destination'] = 'Destination must be at least 3 characters'
        if len(postData['plan']) < 3:
            errors['plan'] = 'Plan must be at least 3 characters'

        # Check for empty start date
        if postData['start_date'] == '':
            errors['start_date_empty'] = 'Please enter a valid start date'
        else:
            # Check for valid start date (in the past)
            if datetime.datetime.strptime(postData['start_date'], '%Y-%m-%d') < datetime.datetime.now():
                errors['start_date_in_past'] = 'Start date cannot be in the past'

        # Check for empty end date
        if postData['end_date'] == '':
            errors['end_date_empty'] = 'Please enter a valid end date'
        else:
            # Check for valid end date (in the past)
            if datetime.datetime.strptime(postData['start_date'], '%Y-%m-%d') < datetime.datetime.now():
                errors['end_date_in_past'] = 'Start date cannot be in the past'

        return errors


class Trip(models.Model):
    destination = models.CharField(max_length=255)
    plan = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, related_name="trips_created", on_delete=models.CASCADE)
    joiners = models.ManyToManyField(
        User, related_name="trips_joined")
    objects = TripManager()
