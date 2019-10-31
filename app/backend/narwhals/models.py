from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=120)
    title = models.TextField()

    def __str__(self):
        return self.name

class Patient(models.Model):
    doctor = models.ForeignKey(Doctor,related_name='patients', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name





class PatientImage(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    imageid = models.IntegerField(primary_key=True)



