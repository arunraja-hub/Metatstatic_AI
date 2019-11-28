from django.contrib import admin
from .models import *
 #Add Doctor DB Model

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(PatientImage)
admin.site.register(PathologyScan)

