# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, View
from django.core.paginator import Paginator
from django.contrib import messages
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Program
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ProgramList(generic.ListView):
    """
    A class to see program pagainated list
    """
    model = Program
    queryset = Program.objects.all().order_by('-id')
    template_name = 'programs_list.html'
    paginated_by = 2

    def get(self, request, *args, **kwargs):
        """
        Function to show
        and paginated all programs
        """
        program_paginator = Paginator(Program.objects.all(), 2)
        page = request.GET.get('page')
        program_list = program_paginator.get_page(page)

        return render(
            request,
            'programs/programs_list.html',
            {'program_list': program_list}
            )


class ProgramDetails(View):
    """
    Class to view more information
    for programs
    """
    def get(self, request, program_id):
        program = Program.objects.get(pk=program_id)

        return render(request, 'programs/programs.html', {'program': program})
