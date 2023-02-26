from django.shortcuts import render
from django.views.generic import View

from .models import Program
from .filters import ProgramFilter


def show_all_programs_page(request):
    context = {}

    filtered_programs = ProgramFilter(
        request.GET,
        queryset=Program.object.all()
    )

    context['filtered_programs'] = filtered_programs

    return render(request, 'programs/programs_list.html', context=context)
