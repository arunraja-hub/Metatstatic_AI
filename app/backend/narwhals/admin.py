from django.contrib import admin
from .models import Doctor #Add Doctor DB Model

# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')

admin.site.register(Doctor, DoctorAdmin)
