from django.db import models
from cloudinary.models import CloudinaryField
from datetime import datetime
from django.core.exceptions import ValidationError

# Create your models here.


def correct_time(self):
    time_entered = Reservation.time
    if time_entered < 5 or time_entered > 9:
        raise ValidationError(
            'Invalid time entered. Please enter a time between 5-9'
            )


def correct_people(self):
    people_entered = Reservation.people
    if people_entered < 1 or people_entered > 8:
        raise ValidationError('Please enter a number between 1-8')


class Reservation(models.Model):
    name = models.CharField(max_length=20,)
    date = models.DateField(default=datetime.now)
    time = models.IntegerField(default="5", validators=[correct_time])
    people = models.IntegerField(default="1", validators=[correct_people])

    def __str__(self):
        return self.name
