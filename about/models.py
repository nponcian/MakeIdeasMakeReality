from django.db import models

# Create your models here.

class MovieEmbed(models.Model):
    title = models.CharField(max_length=100)
    url= models.URLField(max_length=250)

class TechStack(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
