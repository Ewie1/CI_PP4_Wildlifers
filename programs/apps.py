# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.apps import AppConfig
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ProgramsConfig(AppConfig):
    """
    A class for configuring the program app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'programs'
