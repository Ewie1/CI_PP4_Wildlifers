# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect, reverse
from django.views import generic
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

    template_name = 'booking/bookings.html'

    def get(self, request, *args, **kwargs):
        """
        Redirect to login page
        if user is not logged in
        """
        if request.user.is_authenticated:
            email = request.user.email
            program_booking_form = EnrollForm(initial={'email': email})
            return render(
                request,
                'booking/bookings.html',
                {'program_booking_form': program_booking_form}
                )
        else:
            messages.error(
                request, 'You must be Registered or Logged in to Enroll')
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
            program_booking_form = EnrollForm()
            booking.user = request.user
            messages.success(request, 'Your enrollment was Successful!')
            return render(
                request,
                'booking/bookings.html',
                {'program_booking_form': program_booking_form})
        return render(
            request,
            'booking/bookings.html',
            {'program_booking_form': program_booking_form})


class Enrollments(generic.ListView):
    """
    Class to display booking information
    of the logged in user
    """
    model = Enroll
    queryset = Enroll.objects.filter().order_by('-name')
    template_name = 'booking/enrollment_list.html'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        """
        Display logged in user bookings
        paginated by 3 per page
        """
        booking = Enroll.objects.all()
        user = request.user
        paginator = Paginator(Enroll.objects.all(), 2)
        page = request.GET.get('page')
        booking_page = paginator.get_page(page)

        if request.user.is_authenticated:
            enrollments = Enroll.objects.filter(user=request.user)
            return render(
                request,
                'booking/enrollment_list.html',
                {
                    'booking': booking,
                    'enrollments': enrollments,
                    'booking_page': booking_page
                }
            )
        else:
            messages.error(
                request,
                'You must be Registered or Logged in to see Enrollments')
            return render(request, 'home/index.html')


class EditEnrollments(SuccessMessageMixin, UpdateView):
    """
    Class to allow user to
    edit thier enrollments
    """
    model = Enroll
    form_class = EnrollForm
    template_name = 'booking/enrollment_editing.html'
    success_message = 'Update have been successful!'

    def get_success_url(self, **kwargs):
        return reverse('enrollments')


def CancelEnrollments(request, pk):
    """
    Function to delete user
    enrollment individually
    """
    enrollment = Enroll.objects.get(pk=pk)

    if request.method == 'POST':
        enrollment.delete()
        messages.success(request, "Your enrollment have been deleted.")
        return redirect('enrollments')

    return render(
        request,
        'booking/enrollment_delete.html',
        {'enrollment': enrollment}
        )
