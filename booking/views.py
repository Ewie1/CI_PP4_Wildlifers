# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect
from django.views import generic, View
from django.views.generic import ListView, View
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from booking.models import Enroll
from .forms import EnrollForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class EnrollView(View):
    """
    Class view to display booking form
    if user is logged in
    """
    def get(self, request):
        """
        Redirect to login page
        if user is not logged in
        """
        if request.user.is_authenticated:
            program_booking_form = EnrollForm()
            return render(request, 'booking/bookings.html', 
                        {'program_booking_form': program_booking_form})
        else:
            return redirect('accounts/login')

    def post(self, request):
        """
        Validate input information format
        and post to database
        """
        program_booking_form = EnrollForm(data=request.POST)
        
        if program_booking_form.is_valid():
            booking = program_booking_form.save(commit=True)
            booking.save()
            messages.success(request, 'Your are booked in!')
            context = {
                'program_booking_form': program_booking_form
            }

        return render(request, 'booking/bookings.html', context)


class Enrollments(generic.ListView):
    """
    Class to display booking information 
    of the logged in user
    """
    model = Enroll
    queryset = Enroll.objects.filter() 
    template_name = 'enrollment_list.html'
    paginate_by = 3

    def get(self, request):
        """
        Display logged in user bookings 
        paginated by 3 per page
        """
        booking = Enroll.objects.all()
        paginator = Paginator(Enroll.objects.filter(), 3)
        page = request.GET.get('page')
        booking_list = paginator.get_page(page)

        if request.user.is_authenticated:
            enrollments = Enroll.objects.filter(user=request.user)
            return render(request, 'booking/enrollment_list.html',
            {
                'booking': booking,
                'enrollments': enrollments,
                'booking_list': booking_list})
        else:
            return redirect('accounts/login')

        



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