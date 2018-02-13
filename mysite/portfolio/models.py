from django.db import models

class Images(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    image = models.ImageField()

# Create your models here.
