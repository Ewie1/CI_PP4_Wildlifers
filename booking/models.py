# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


available_times = (
    ('09:00', '09:00'),
    ('11:00', '11:00'),
    ('13:00', '13:00'),
    ('15:00', '15:00'),
    ('17:00', '17:00'),
    ('19:00', '19:00'),
)


volunteer_jobs = (
    ('Identify Animals', 'Identify Animals'),
    ('Fund Raiser', 'Fund Raiser'),
    ('Transcribe Field Notes', 'Transcribe Field Notes'),
    ('Help Researchers', 'Help Researchers'),
)


class Enroll(models.Model):
    """
    Model for Program bookings
    """
    
    start_date = models.DateField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user", null=True)
    name = models.CharField(
        max_length=50,
        null=True
        )
    email = models.EmailField(
        max_length=254,
        default=""
        )
    volunteer_job = models.CharField(
        max_length=100,
        choices=volunteer_jobs,
        default=''
    )
    work_time = models.CharField(
        max_length=50,
        choices=available_times,
        default=''
    )

    class Meta:
        ordering = ['-name']
        unique_together = ('work_time', 'volunteer_job')

    def __str__(self):
        return self.name
