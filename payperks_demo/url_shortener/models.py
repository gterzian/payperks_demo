from django.db import models


class ShortenedURL(models.Model):

    original = models.CharField(max_length=5000, unique=True)
    shortened = models.CharField(max_length=5000, null=True)
    
