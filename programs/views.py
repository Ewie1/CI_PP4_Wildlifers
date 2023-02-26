from django.shortcuts import render

from .models import Program
from .filters import ProgramFilter


def show_all_programs_page(request):
    context = {}

    filtered_programs = ProgramFilter(
        request.GET,
        queryset=Program.object.all()
    )

    context['filtered_programs'] = filtered_programs.qs 

    return render(request, '', context=context)
