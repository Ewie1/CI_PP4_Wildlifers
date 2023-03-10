from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_all_programs_page, name='programs'),
    path('show_program/<program_id>', views.ProgramDetails.as_view(), name='show_program')
]