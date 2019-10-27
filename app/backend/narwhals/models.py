from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=120)
    title = models.TextField()

    def __str__(self):
        return self.name

