import tensorflow as tf
import numpy as np
from tensorflow import keras

image = tf.keras.preprocessing.image
model = keras.models.load_model('models/eyes.h5')

class_ = ['black','blue','brown']

def classifyEyes(image_fp):
    img = image.load_img(image_fp, target_size = (400, 540))
    img = image.img_to_array(img)

    image_array = img / 255. # scale the image
    img_batch = np.expand_dims(image_array, axis = 0)

    predicted_value = model.predict(img_batch)

    out  = {
               "label": f"{class_[predicted_value.argmax()]}",
      "accuracy_score": f"{predicted_value[0][predicted_value.argmax()]}",
    }
    return out