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

    def __str__(self):
        return self.name


#class StartDate(models.Model):
#    start_date = models.DateField()


#class ProgramBooking(models.Model):
#    booking_id = models.AutoField(primary_key=True)
#    name = models.CharField(
#        max_length=50,
#        null=True
#        )
#    user = models.ForeignKey(
#        User, on_delete=models.CASCADE, related_name="", null=True)
 #   animal_name = models.CharField(unique=True)
#    animal_country = CountryField()
#    email = models.EmailField(
#        max_length=254,
#        default=""
#        )
 #   start_date = models.DateField()

#   class Meta(self):
 #       ordering = ('-created_on')    
#        def __str__(self):
#            return self.name


#class ProgramCheckIn(models.Model):
#    check_in_date = models.DateField(unique=True)
#    check_in_time = models.CharField(
#        max_length=20,
 #       choices=available_times,
#        default='08:00',
#        unique=True
#        )
    
#    class Meta (self):
#        ordering = ('-created-on')

#    def __str__(self):
#        return self.check_in_time

#class Enroll(models.Model):
#    name = models.CharField(max_length=50)
#    date = models.DateField()
#    time = models.TimeField()
#    animal = modesl.CharField()
    

#    def __str__(self):
#        return self.name