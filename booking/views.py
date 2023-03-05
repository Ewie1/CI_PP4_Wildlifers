from django.shortcuts import render

from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib import messages
from booking.models import Enroll
from .forms import EnrollForm


class EnrollView(View):

    def get(self, request, *args, **kwargs):
        program_booking_form = EnrollForm()

        return render(request, 'booking/bookings.html', 
                        {'program_booking_form': program_booking_form})

    def post(self, request):
        program_booking_form = EnrollForm(data=request.POST)
        
        if program_booking_form.is_valid():
            reservation = program_booking_form.save(commit=True)
            reservation.save()
            messages.success(request, 'Your are booked in!')
            context = {
                'program_booking_form': program_booking_form
            }

        return render(request, 'booking/bookings.html', context)

#def EnrollView(request):
#    booking = EnrollForm()

#    if request.method == 'POST':
#        booking = EnrollForm(request.POST)

#        if booking.is_valid():
 #           reservation = booking.save(commit=True)
#            reservation.save()
#            messages.success(request, 'Your are booked in!')
            
#    context = {
#        'booking': booking
#    }
#    return render(request, 'booking/bookings.html', context)