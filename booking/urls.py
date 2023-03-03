from django.urls import path

from booking import views

urlpatterns = [
    path('', views.EnrollView, name='booking')
]
