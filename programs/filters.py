import django_filters

from .models import Program


class ProgramFilter(django_filters.Filterset):
    """
    Class to filter Program
    """
    class meta:
        model = Program
        fields = [
            'name',
            'country',
            'category',
        ]
