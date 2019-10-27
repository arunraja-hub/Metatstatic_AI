from django.shortcuts import render
from rest_framework import generics
from .serializers import DoctorSerializer
from .models import Doctor

class DoctorList(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class DoctorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
# Create your views here.
