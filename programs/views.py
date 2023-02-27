from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator


from .models import Program
from .filters import ProgramFilter


def show_all_programs_page(request):
    context = {}

    filtered_programs = ProgramFilter(
        request.GET,
        queryset=Program.objects.all()
    )

    context['filtered_programs'] = filtered_programs

    paginated_filtered_programs = Paginator(filtered_programs.qs, 8)

    page_number = request.GET.get('page')
    program_page_obj = paginated_filtered_programs.get_page(page_number)

    context['program_page_obj'] = program_page_obj
    context['all_programs'] = Program.objects.all()

    return render(request, 'programs/programs_list.html', context)


