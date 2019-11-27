from rest_framework import serializers
from .models import Doctor, Patient, PatientImage
from .patientImageSerializer import PatientImageSerializer

class PatientSerializer(serializers.ModelSerializer):
    patient_image = PatientImageSerializer(many=True, read_only=False)
    class Meta:
        model = Patient
        fields = ['id','doctor','name','histologic_grade','ml_prediction','pathology_report','last_modified', 'patient_image']