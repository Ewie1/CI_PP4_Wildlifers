# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Create your models here.


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


class Country (models.Model):
    """
    Class for animal's country
    """
    country = CountryField(blank=True)

    def __str__(self):
        """
        Return animal's country name
        """
        return self.country


class Survival_cateogory (models.Model):
    """
    Class for animal's country
    """
    cateogory = models.CharField(
        max_length=50, unique=True)

    def __str__(self):
        """
        Return animal's cateogory
        """
        return self.cateogory


class Program(models.Model):
    """
    Class for program list
    """

    animal_name = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE
        )
    animal_cateogory = models.ForeignKey(
        Survival_cateogory,
        on_delete=models.CASCADE)
    description = models.TextField()
    country = CountryField(blank=True)
    image = CloudinaryField(
        'image',
        default='placeholder')
