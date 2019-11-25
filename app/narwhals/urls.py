# todos/urls.py
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework import routers
from .api import PatientViewSet, DoctorViewSet, PatientImageView

router = routers.DefaultRouter()
router.register('api/patients', PatientViewSet, 'patients')
router.register('api/doctors', DoctorViewSet, 'doctors')

urlpatterns = [
    path('api/patientImages/<int:pk>/', PatientImageView.as_view())
]

urlpatterns += router.urls

