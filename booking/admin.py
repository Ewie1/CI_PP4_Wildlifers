# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from booking.models import Enroll
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@admin.register(Enroll)
class EnrollAdmin(admin.ModelAdmin):
    """
    A class for admin to manage Enrollments
    """
    list_filter = (
        'user',
        'start_date',
        'email',
        'animal_name',
        'volunteer_job',
        'work_time',
        'created_date'
    )

    list_display = (
        'user',
        'start_date',
        'email',
        'animal_name',
        'volunteer_job',
        'work_time',
        'created_date'
    )

    search_fields = ('user', 'animal_name')
