from django.contrib import admin

from booking.models import ProgramSelection, ProgramCheckIn, StartDate

admin.site.register(ProgramCheckIn)
admin.site.register(ProgramSelection)
admin.site.register(StartDate)
