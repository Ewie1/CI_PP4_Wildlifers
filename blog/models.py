from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'DRAFT'), (1, 'POST'))


class Post(models.Model):
    """
    Class for site blog
    """
    title = models.CharField(max_length=255)
    