from rest_framework import serializers
from .models import Doctor, Patient, PatientImage
from .patientSerializer import PatientSerializer


class PatientImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientImage
        fields = ('pid', 'imageid')

