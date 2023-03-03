from django.urls import path

from booking import views

urlpatterns = [
    path('', views.Booking.as_view(), name='bookings')
]
