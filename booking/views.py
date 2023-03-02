from django.shortcuts import render

from django.views import generic, View
from django.contrib.auth.models import User

from .models import ProgramBooking, ProgramCheckIn
from .forms import ProgramBookingForm, ProgramCheckInForm


class Booking(View):
    def post(self, request):
        program_booking_form = ProgramBookingForm(data=request.POST)
        
        if program_booking_form.is_valid():
            reservation = program_booking_form.save(commit=True)
            reservation.save()
            messages.success(request, 'Your are booked in!')
    context = {
        'program_booking_form': program_booking_form
        }

    return render(request, '', context)

