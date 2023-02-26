# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


# Internal
from .models import Animal, Country, Survival_category, Program
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

admin.site.register(Animal)
admin.site.register(Country)
admin.site.register(Survival_category)


@admin.register(Program)
class ProgramAdmin(SummernoteModelAdmin):
    """
    Admin class for Program model
    """
    list_display = (
        'animal_name',
        'animal_category',
        'country',
    )
    search_fields = ('name')
    summernote_fields = ('description')
