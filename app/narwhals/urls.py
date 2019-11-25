# todos/urls.py
from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from rest_framework import routers
from .api import PatientViewSet, DoctorViewSet, PatientImageViewSet, GCPImage

router = routers.DefaultRouter()
router.register('api/patients', PatientViewSet, 'patients')
router.register('api/doctors', DoctorViewSet, 'doctors')
router.register('api/patientsImages', PatientImageViewSet, 'patientsImages')

urlpatterns = [
     path('api/gcpImages/<int:pk>/', GCPImage.as_view())
]

urlpatterns += router.urls

