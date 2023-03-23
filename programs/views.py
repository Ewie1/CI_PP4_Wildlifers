# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from django.contrib import messages
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Program
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def show_all_programs_page(request):
    """
    Function to show 
    and paginted all programs
    """
    program_paginator = Paginator(Program.objects.all(), 3)
    page = request.GET.get('page')
    program_list = program_paginator.get_page(page)

    return render(request, 'programs/programs_list.html',
        {'program_list': program_list})


class ProgramDetails(View):
    """
    Class to view more information
    for programs
    """
    def get(self, request, program_id):
        program = Program.objects.get(pk=program_id)

        return render(request, 'programs/programs.html', {'program': program})
    