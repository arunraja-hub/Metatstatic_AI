from __future__ import absolute_import, division, print_function, unicode_literals

import os

import tensorflow as tf
from tensorflow import keras

import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import convertapi



model=tf.keras.models.load_model('proto_model.h5')
model.load_weights('proto_model.h5')
#new_model.summary()



# predicting single image


model.summary()

model.compile(lr=0.0001, loss='binary_crossentropy', 
              metrics=['accuracy'])



from PIL import Image
im = Image.open('1_17.tif')
im.save('test2.jpg')

img = image.load_img('test2.jpg', target_size=(96, 96))
#, target_size=(96, 96)
x = image.img_to_array(img)
print(x.shape)
x = np.expand_dims(x, axis=0)
print(x.shape)
#images = np.vstack([x])
##print(images)
classes = model.predict(x)
print ('pred',classes)