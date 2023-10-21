import tensorflow as tf
from tensorflow.keras.preprocessing import image as keras_image
from PIL import Image
import numpy as np

lbls = ['Bacterial Spot',
        'Early Blight',
        'Late Blight',
        'Leaf Mold',
        'Septoria Leaf Spot',
        'Target Spot',
        'Tomato Yellow Leaf Curl Virus',
        'Tomato Mosaic Virus',
        'Two-Spotted Spider Mite',
        'Healthy']

model = tf.keras.models.load_model('90plus.h5', compile=False)

def make_prediction(img):
    img = img.resize((227, 227))
    img = img.convert("RGB")
    img_array = keras_image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    prediction_label = np.argmax(prediction)
    prediction_val = prediction[0][prediction_label]
    if prediction_val<0.1:
        return {}
    else:
        return {"name":lbls[prediction_label], "probability":round(float(prediction[0][prediction_label]), 4)}