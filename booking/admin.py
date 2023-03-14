# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from booking.models import Enroll
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


admin.site.register(Enroll)

@admin.register(Enroll)
class EnrollAdmin(admin.ModelAdmin):
    list_filter = (
        'user',
        'start_date',
        'email',
        'animal_name',
        'volunteer_job',
        'work_time',
        'created_on'
    )

    list_display = (
        'user',
        'start_date',
        'email',
        'animal_name',
        'volunteer_job',
        'work_time',
        'created_on'
    )

     