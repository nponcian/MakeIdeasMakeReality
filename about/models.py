from django.db import models

# Create your models here.

class MovieEmbed(models.Model):
    title = models.CharField(max_length=100)
