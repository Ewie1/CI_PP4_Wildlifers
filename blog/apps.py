# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.apps import AppConfig
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class BlogConfig(AppConfig):
    """
    A class for configuring the blog app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
