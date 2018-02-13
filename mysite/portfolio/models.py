from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.name

# Create your models here.
