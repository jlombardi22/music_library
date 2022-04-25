from django.db import models

# Create your models here.


class Songs(models.Model):
    title = models.CharField(max_length=255, null=True)
    artist = models.CharField(max_length=255, null=True)
    album = models.CharField(max_length=255, null=True)
    release_date = models.CharField(max_length=255, null=True)
    genre = models.CharField(max_length=255, null=True)
