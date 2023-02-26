from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_all_programs_page, name='programs')
]