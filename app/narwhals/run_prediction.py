

def cnn_predict(srcfile):

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

    ml_prediction_Dir = "./ml_prediction"
    first_layer_dir = filename.replace('.tif', '')
    second_layer_dir = filename.replace('.tif', '') + "_2"
    dataFlowDir = ml_prediction_Dir + "/" + first_layer_dir
    ml_prediction_Dir += "/" + first_layer_dir + "/" + second_layer_dir

    if not os.path.exists(ml_prediction_Dir):
        os.makedirs(ml_prediction_Dir)

    destfile = ml_prediction_Dir + "/" + filename
    shutil.copyfile(srcfile, destfile)

    datagen = ImageDataGenerator(rescale=1.0/255)
    model = tensorflow.keras.models.load_model('./static/final_model.h5')
    model.load_weights('./static/final_model_weights.h5')
    pred_gen = datagen.flow_from_directory(dataFlowDir,
                                            #Our Testing Data from Kaggle 96 x 96
                                            target_size=(96,96),
                                            batch_size=1,
                                            class_mode='categorical',
                                            shuffle=False)
    predictions = model.predict_generator(pred_gen, steps=1, verbose=1)
    print(predictions)
    print(predictions[0][1])
    return predictions[0][1]
