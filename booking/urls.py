from django.urls import path

from booking import views

urlpatterns = [
    path('enrollview', views.EnrollView.as_view(), name='enrollview')
]
