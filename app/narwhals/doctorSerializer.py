from rest_framework import serializers
from .models import *
from .patientSerializer import PatientSerializer

class DoctorSerializer(serializers.ModelSerializer):
    patients = PatientSerializer(many=True, read_only=False, required=False)
    class Meta:
        model = Doctor
        fields = ['id','name', 'title', 'patients']