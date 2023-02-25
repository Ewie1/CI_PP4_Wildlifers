from django.db import models
from cloudinary.models import CloudinaryField

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
    country = models.CharField(
        max_length=50, unique=True)

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
        return self.country


class Programs(models.Model):
    """
    Class for program list
    """

    name = models.CharField(
        max_length=50, unique=True)
    description = models.TextField()
    country = models.CharField(max_length=50)
    image = models.CloudinaryField(
        'image', default='placeholder')
