from django.apps import AppConfig
import html
import pathlib
import os
from .metastaticPredictor import MetastaticPredictor


class NarwhalsConfig(AppConfig):
    name = 'narwhals'
    MODEL_PATH = pathlib.Path("./ml_model")
    METASTATIC_AI_MODEL_PATH = "ml_model/final_model.h5"
    METASTATIC_AI_MODEL_WEIGHTS_PATH = "ml_model/final_model_weights.h5"
    ML_PREDICTION_PROCESSING_PATH = pathlib.Path("ml_prediction_processing")
    predictor = MetastaticPredictor(METASTATIC_AI_MODEL_PATH, METASTATIC_AI_MODEL_WEIGHTS_PATH, ML_PREDICTION_PROCESSING_PATH)
