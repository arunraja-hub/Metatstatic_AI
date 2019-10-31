from rest_framework import serializers
from .models import Doctor, Patient, PatientImage

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id','name','histologic_grade','ml_prediction','pathology_report','last_modified']