# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Animal (models.Model):
    """
    Class for animal name
    """
    name = models.CharField(
        max_length=50, unique=True)

    def __str__(self):
        """
        Return animal name
        """
        return self.name


class Survival_category (models.Model):
    """
    Class for animal's country
    """
    category = models.CharField(
        max_length=50)

    def __str__(self):
        """
        Return animal's category
        """
        return self.category


class Program(models.Model):
    """
    Class for program list
    """

    animal_name = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        )
    animal_category = models.ForeignKey(
        Survival_category,
        on_delete=models.CASCADE)
    description = models.TextField()
    country = CountryField()
    image = CloudinaryField(
        'image',
        default='placeholder')
