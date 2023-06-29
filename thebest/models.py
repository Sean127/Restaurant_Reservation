from django.db import models
from cloudinary.models import CloudinaryField
from datetime import datetime
from django.core.exceptions import ValidationError

# Create your models here.


# Create your models here.
TIME_CHOICES = (
   ("5 PM", "5 PM"),
   ("5:30 PM", "5:30 PM"),
   ("6 PM", "6 PM"),
   ("6:30 PM", "6:30 PM"),
   ("7 PM", "7 PM"),
   ("7:30 PM", "7:30 PM"),
   ("8 PM", "8 PM"),
   ("8:30 PM", "8:30 PM"),
   ("9 PM", "9 PM")
)

PEOPLE = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
)


class Reservation(models.Model):
    name = models.CharField(max_length=20,)
    date = models.DateField(default=datetime.now)
    time = models.CharField(
        max_length=10, choices=TIME_CHOICES, default="5 PM")
    people = models.CharField(max_length=5, choices=PEOPLE, default="1")

    def __str__(self):
        return self.name

    def clean_date(self):
        date = self.Reservation['date']
        if date < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        return date
