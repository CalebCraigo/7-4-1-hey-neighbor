from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class Tool(models.Model):

    AVAILABLE_TYPES = [
    ('YARD', 'Yard'),
    ('WOODWORKING', 'Woodworking'),
    ('PLUMBING', 'Plumbing'),
    ('AUTO', 'Auto')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tool = models.CharField(max_length=255, default='')
    types = models.CharField(max_length=255, choices=AVAILABLE_TYPES, default='YARD')
    date_posted = models.DateTimeField('Date Posted', default=timezone.now)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.tool

    def get_absolute_url(self):
        return reverse('hey_neighbor:index')


# Create your models here.
