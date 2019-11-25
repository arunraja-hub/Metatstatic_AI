from .models import Patient, Doctor, PatientImage
from rest_framework import viewsets, permissions
from .patientSerializer import PatientSerializer
from .doctorSerializer import DoctorSerializer
from .patientImageSerializer import PatientImageSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = PatientSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = DoctorSerializer

# class PatientImageViewSet(viewsets.ModelViewSet):
#     queryset = PatientImage.objects.all()
#     permissions_classes = [
#         permissions.AllowAny
#     ]
#     serializer_class = PatientImageSerializer

class PatientImageView(APIView):
    """
    List all patientsImages based on PatientID.
    """
    def get_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except PatientImage.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data.get('patient_image'))
