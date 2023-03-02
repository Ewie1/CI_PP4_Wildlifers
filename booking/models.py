from django.db import models


#class ProgramSelection(models.Model):
#    animal_name = models.CharField()

available_times = (
    ('09:00'),
    ('11:00'),
    ('13:00'),
    ('15:00'),
    ('17:00'),
    ('19:00'),
)


#class StartDate(models.Model):
#    start_date = models.DateField()


class ProgramBooking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=50,
        null=True
        )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="", null=True)
    animal_name = models.CharField()
    email = models.EmailField(
        max_length=254,
        default=""
        )
    start_date = models.DateField()


class ProgramCheckIn(models.Model):
    check_in_date = models.DateField()
    check_in_time = modesl.CharField(
        max_length=20,
        choices=available_times,
        default='08:00'
        )
    