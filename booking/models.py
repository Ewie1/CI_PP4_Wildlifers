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

animal_names = (
    ('Red Panda', 'Red Panda'),
    ('Artic Fox', 'Artic Fox'),
    ('Giant Panda', 'Giant Panda'),
    ('Red Wolf', 'Red Wolf'),
    ('Persian Fallow Dear', 'Persian Fallow Dear'),
    ('Saola', 'Saola'),
    ('Amur Leopard', 'Amur Leopard'),
    ('Arctic Beluga', 'Arctic Beluga'),
    ('Hyacinth Macaw', 'Hyacinth Macaw'),
    ('Vaquita', 'Vaquita'),
    ('Lemur', 'Lemur'),
)


class Enroll(models.Model):
    """
    Model for Program bookings
    """
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    start_date = models.DateField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user", null=True)
    name = models.CharField(
        max_length=30,
        null=True
        )
    email = models.EmailField(
        max_length=254,
        default=""
        )
    volunteer_job = models.CharField(
        max_length=30,
        choices=volunteer_jobs,
        blank=False
    )
    work_time = models.CharField(
        max_length=50,
        choices=available_times,
        blank=False
    )
    animal_name = models.CharField(
        max_length=30,
        choices=animal_names,
        blank=False
        )

    class Meta:
        ordering = ['-name']
        unique_together = (
            'work_time',
            'volunteer_job',
            'animal_name',
            'start_date',
            )

    def __str__(self):
        return self.name
