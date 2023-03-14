# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Enroll
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class DateInput(forms.DateInput):
    """
    Class for date input
    """
    input_type = 'date'


class EnrollForm(forms.ModelForm):
    """
    Class for user detail form
    """
    class Meta:
        model = Enroll
        fields = [
            'user',
            'start_date',
            'email',
            'volunteer_job',
            'work_time',
            'animal_name'
            ]
        widgets = {
            'start_date': DateInput(),
        }
