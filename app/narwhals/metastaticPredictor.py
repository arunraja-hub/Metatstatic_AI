class MetastaticPredictor:

    def __init__(self, model_path, weights_path, ml_prediction_processDir):
        import tensorflow
        from tensorflow import keras
        from keras.preprocessing.image import ImageDataGenerator
        from keras.models import load_model
        import cv2
        import os
        import shutil
        self.model_path = model_path
        self.weights_path = weights_path
        self.ml_prediction_processDir = ml_prediction_processDir
        self.model = tensorflow.keras.models.load_model(model_path)
        self.model.load_weights(weights_path)
        self.datagen = ImageDataGenerator(rescale=1.0/255)

    def predict(self, srcfile):
        import tensorflow
        from tensorflow import keras
        from keras.preprocessing.image import ImageDataGenerator
        from keras.models import load_model
        import cv2
        import os
        import shutil
        #Return a Percentage of Getting the Cancer

        #srcfile = "C:\\Users\\LAI\\Desktop\\Narwhals\\app\\narwhals\\12.tif"
        filename = os.path.basename(srcfile)
        print(filename)

        ml_prediction_Dir = self.ml_prediction_processDir
        first_layer_dir = filename.replace('.tif', '')
        second_layer_dir = filename.replace('.tif', '') + "_2"
        dataFlowDir = os.path.join(ml_prediction_Dir,first_layer_dir)
        ml_prediction_Dir = os.path.join(dataFlowDir, second_layer_dir)

        if not os.path.exists(ml_prediction_Dir):
            os.makedirs(ml_prediction_Dir)

        destfile = os.path.join(ml_prediction_Dir, filename)
        shutil.copyfile(srcfile, destfile)

        pred_gen = self.datagen.flow_from_directory(dataFlowDir,
                                                #Our Testing Data from Kaggle 96 x 96
                                                target_size=(96,96),
                                                batch_size=1,
                                                class_mode='categorical',
                                                shuffle=False)
        predictions = self.model.predict_generator(pred_gen, steps=1, verbose=1)
        print(predictions)
        print(str(round(predictions[0][1],2)))
        result = str(round(predictions[0][1],4))
        return float(result)
