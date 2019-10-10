from django.db import models
from django.utils import timezone
from django.urls import reverse

class Tools(models.Model):

    AVAILABLE_TYPES = [
    ('YARD', 'Yard'),
    ('WOODWORKING', 'Woodworking'),
    ('PLUMBING', 'Plumbing'),
    ('AUTO', 'Auto')
    ]

    tool = models.CharField(max_length=255, default='')
    types = models.CharField(max_length=255, choices=AVAILABLE_TYPES, default='YARD')
    date_posted = models.DateTimeField('Date Posted', default=timezone.now)

    def __str__(self):
        return self.tool


# Create your models here.
