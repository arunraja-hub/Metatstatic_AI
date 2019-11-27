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
    histologic_grade = models.IntegerField(default=0)
    ml_prediction = models.FloatField(default=0.0)
    pathology_report = models.TextField(default='HyperLink')
    last_modified = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name


class PatientImage(models.Model):
    patient = models.ForeignKey(Patient,related_name='patient_image',on_delete=models.CASCADE)
    imagefile = models.CharField(max_length=500)
    ml_prediction = models.FloatField(default=0.0)
    last_modified = models.DateField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.imagefile



