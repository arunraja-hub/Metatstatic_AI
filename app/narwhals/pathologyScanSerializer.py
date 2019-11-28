from rest_framework import serializers
from .models import *
from .tif_conversion import *
import os

class PathologyScanSerializer(serializers.ModelSerializer):

    jpg_file = serializers.SerializerMethodField('get_jpg_file')

    class Meta:
        model = PathologyScan
        fields = ['id','name','pathology_Main_Img','patient','ml_prediction','jpg_file','last_modified']

    def get_jpg_file(self, obj):
        srcFile = obj.pathology_Main_Img.path
        filename = obj.pathology_Main_Img.name.replace('.tif', '.jpg')
        destDir = '/media/jpg_images/'
        if not os.path.exists(destDir):
            os.makedirs(destDir)
        convertTifToJpg(srcFile, destDir)
        return destDir+filename
