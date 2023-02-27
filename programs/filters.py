import django_filters

from .models import Program


class ProgramFilter(django_filters.FilterSet):
    """
    Class to filter Program
    """
    name = django_filters.CharFilter(lookup_expr='icontains', label="Name")
    country = django_filters.CharFilter(
        lookup_expr='icontains',
        label="Country")
    
    category = django_filters.CharFilter(
        lookup_expr='icontains',
        label="Category")

    class meta:
        model = Program
        fields = ['name', 'country', 'category',]
