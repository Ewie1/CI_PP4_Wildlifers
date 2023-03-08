from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator


from .models import Program
#from .filters import ProgramFilter


#def show_all_programs_page(request):
#    context = {}

#    filtered_programs = ProgramFilter(
#        request.GET,
#        queryset=Program.objects.all()
#    )

#    context['filtered_programs'] = filtered_programs

 #   paginated_filtered_programs = Paginator(filtered_programs.qs, 1)

#    page_number = request.GET.get('page')
#    program_page_obj = paginated_filtered_programs.get_page(page_number)

#    context['program_page_obj'] = program_page_obj
#    context['all_programs'] = Program.objects.all()

#   return render(request, 'programs/programs_list.html', context)


def show_all_programs_page(request):
    """
    Function to show 
    and paginte all programs
    """
    program_paginator = Paginator(Program.objects.all(), 5)
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

