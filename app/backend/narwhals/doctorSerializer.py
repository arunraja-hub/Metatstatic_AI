from rest_framework import serializers
from .models import Doctor, Patient, PatientImage
from .patientSerializer import PatientSerializer

class DoctorSerializer(serializers.ModelSerializer):
    patients = PatientSerializer(many=True,read_only=True)
    class Meta:
        model = Doctor
        fields = ['id','name', 'title', 'patients']