from .models import Patient, Doctor, PatientImage
from rest_framework import viewsets, permissions, generics, filters
from .patientSerializer import PatientSerializer
from .doctorSerializer import DoctorSerializer
from .patientImageSerializer import PatientImageSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from url_filter.integrations.drf import DjangoFilterBackend
from .gcp_operations import download_subdir,upload_file
from .tif_conversion import convertTifToJpg
import os

gcp_bucket = "patients_image"

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

class PatientImageViewSet(viewsets.ModelViewSet):
    queryset = PatientImage.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = PatientImageSerializer
    filterset_fields = ['patient', 'imagefile']

class GCPImage(APIView):
    """
    Retrieve, update or delete a Patient Image instance.
    """
    def get_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient)
        image_list = serializer.data.get('patient_image')
        subdir = str(pk) + "/"
        dl_localdir = "narwhals/static/media/" + subdir
        os.makedirs(dl_localdir, exist_ok=True)
        download_subdir(gcp_bucket, subdir, dl_localdir)
        for image in image_list:
            curFilePath = dl_localdir + str(pk) + '_'+ image.get('imagefile')
            convertTifToJpg(curFilePath,dl_localdir)
        return Response(image_list)



