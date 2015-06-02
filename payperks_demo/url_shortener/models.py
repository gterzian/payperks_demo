from django.db import models


class ShortenedURL(models.Model):

    original = models.CharField(max_length=5000)
    shortened = models.CharField(max_length=5000)
    
