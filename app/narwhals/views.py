from django.shortcuts import render
from rest_framework import generics
from .patientSerializer import PatientSerializer
from .doctorSerializer import DoctorSerializer
from .models import Doctor, Patient
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

class DoctorList(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class DoctorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class PatientList(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class PatientDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer





# Create your views here.
