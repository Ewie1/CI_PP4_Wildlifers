# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect, reverse
from django.views import generic, View
from django.views.generic import ListView, View
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from booking.models import Enroll
from .forms import EnrollForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def get_user_instance(request):
    """
    Get logged in user details
    """
    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()
    return user


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
            email = request.user.email
            program_booking_form = EnrollForm(initial={'email': email})
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
            booking = program_booking_form.save(commit=False)
            booking.user = request.user
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
    queryset = Enroll.objects.filter().order_by('id')
    template_name = 'enrollment_list.html'
    paginate_by = 3

    def get(self, request):
        """
        Display logged in user bookings 
        paginated by 3 per page
        """
        booking = Enroll.objects.all()
        paginator = Paginator(Enroll.objects.filter(user=request.user), 3)
        page = request.GET.get('page')
        booking_page = paginator.get_page(page)

        if request.user.is_authenticated:
            enrollments = Enroll.objects.filter(user=request.user)
            return render(request, 'booking/enrollment_list.html',
            {
                'booking': booking,
                'enrollments': enrollments,
                'booking_page': booking_page})
        else:
            return redirect('accounts/login')


class EditEnrollments(SuccessMessageMixin, UpdateView):
    """
    Class to allow user to
    edit thier enrollments
    """
    model = Enroll
    form_class = EnrollForm
    template_name = 'booking/enrollment_editing.html'
    success_message = 'hey'

    def get_success_url(self, **kwargs):
        return redirect('enrollments') 


def CancelEnrollments(request, pk):
    """
    Function to delete user
    enrollment individually
    """
    delete_enrollment = Enroll.objects.get(pk=pk)

    if request.method == 'POST':
        delete_enrollment.delete()
        messages.success(request, "Your plan has been deleted.")
        return redirect('enrollments')
    else:
        messages.error(request,
                        'An error occurred when deleting your plan.')   
    return redirect('enrollments')
