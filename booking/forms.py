from django import forms

from .models import ProgramBooking, ProgramCheckIn


class ProgramBookingForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'min': datetime.now().date()}))

    class Meta(self):
        model = ProgramBooking
        fields = (
            'name',
            'user',
            'animal_name',
            'country_name',
            'email',
            'start_date'
        )


class ProgramCheckInForm(forms.ModelForm):
    check_in_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'min': datetime.now().date()}))

    class Meta(self):
        model = ProgramCheckIn
        fields = (
            'check_in_date',
            'check_in_time'
        )
