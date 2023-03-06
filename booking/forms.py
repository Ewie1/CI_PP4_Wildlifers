# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Enroll
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#class ProgramBookingForm(forms.ModelForm):
#    start_date = forms.DateField(
#        widget=forms.DateInput(
#            attrs={'type': 'date', 'min': datetime.now().date()}))

#    class Meta(self):
#        model = ProgramBooking
#        fields = (
#            'name',
#            'user',
#            'animal_name',
#            'country_name',
#            'email',
#            'start_date'
#        )


#class ProgramCheckInForm(forms.ModelForm):
#    check_in_date = forms.DateField(
#        widget=forms.DateInput(
#            attrs={'type': 'date', 'min': datetime.now().date()}))

#    class Meta(self):
#        model = ProgramCheckIn
#        fields = (
#            'check_in_date',
#            'check_in_time'
#        )

class DateInput(forms.DateInput):
    """
    Class for date input
    """
    input_type = 'date'


class EnrollForm(forms.ModelForm):
    """
    Class for Enrollment form
    """
    class Meta:
        model = Enroll
        fields = [
            'name',
            'start_date',
            'email',
            'volunteer_job',
            'work_time'
            ]
        widgets = {
            'start_date': DateInput(),
        }

