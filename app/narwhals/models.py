from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=120)
    title = models.TextField()

    def __str__(self):
        return self.name

class Patient(models.Model):
    doctor = models.ForeignKey(Doctor,related_name='patients', on_delete=models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=120)
    histologic_grade = models.IntegerField(default=0)
    ml_prediction = models.FloatField(default=0.0)
    pathology_report = models.TextField(default='HyperLink')
    last_modified = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name


class PatientImage(models.Model):
    patient = models.ForeignKey(Patient,related_name='patient_image',on_delete=models.DO_NOTHING, blank=True, null=True)
    imagefile = models.ImageField(upload_to='images/')
    ml_prediction = models.FloatField(default=0.0)
    serverFilePath = models.CharField(max_length=100, blank=True, null=True)
    last_modified = models.DateField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.imagefile

class PathologyScan(models.Model):
    name = models.CharField(max_length=100)
    pathology_Main_Img = models.FileField(upload_to='images/', blank=False, null=False)
    patient = models.ForeignKey(Patient,related_name='pathology_images',on_delete=models.DO_NOTHING, blank=True, null=True)
    ml_prediction = models.FloatField(default=0.0)
    jpg_file = models.CharField(max_length=100, blank=True, null=True)
    last_modified = models.DateField(auto_now=True, auto_now_add=False) 
    def __str__(self):
        return self.name



