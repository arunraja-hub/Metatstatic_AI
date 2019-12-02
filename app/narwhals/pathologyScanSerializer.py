from rest_framework import serializers
from .models import *
from .tif_conversion import *
import os
from .run_prediction import *
from .apps import NarwhalsConfig

class PathologyScanSerializer(serializers.ModelSerializer):

    jpg_file = serializers.SerializerMethodField('get_jpg_file')
    ml_prediction = serializers.SerializerMethodField('get_ml_prediction')

    class Meta:
        model = PathologyScan
        fields = ['id','name','pathology_Main_Img','patient','ml_prediction','jpg_file','last_modified']

    def get_jpg_file(self, obj):
        if obj.jpg_file is None:
            srcFile = obj.pathology_Main_Img.path
            filename = os.path.basename(srcFile)
            filename = filename.replace('.tif', '.jpg')
            destDir = 'build/media/images/'
            if not os.path.exists(destDir):
                os.makedirs(destDir)
            convertTifToJpg(srcFile, destDir)
            jpgPath = obj.pathology_Main_Img.url.replace('.tif', '.jpg')
            return jpgPath
        return obj.jpg_file

    def get_ml_prediction(self, obj):
        if obj.ml_prediction == 0.0:
            srcFile = obj.pathology_Main_Img.path
            ml_score = NarwhalsConfig.predictor.predict(srcFile) * 100
            print(ml_score)
            return ml_score
        return obj.ml_prediction
