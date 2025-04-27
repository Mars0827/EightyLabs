import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v3 import preprocess_input
from PIL import Image
import streamlit as st

@st.cache_resource
def load_classification_model(model_path="capstone1mobilenetsv3.h5", compile=False):
    return load_model(model_path)

def load_and_preprocess_image(img_file, target_size=(224, 224)):
    img = Image.open(img_file).convert('RGB')
    img_resized = img.resize(target_size)
    img_array = image.img_to_array(img_resized)
    img_array = np.expand_dims(img_array, axis=0)
    processed_img = preprocess_input(img_array)
    return img, processed_img

def predict(model, processed_img, class_names):
    predictions = model.predict(processed_img)
    if len(predictions.shape) > 1 and predictions.shape[1] > 1:
        predicted_class_idx = np.argmax(predictions[0])
        confidence = predictions[0][predicted_class_idx]
        predicted_class = class_names[predicted_class_idx]
    else:
        confidence = predictions[0][0]
        predicted_class_idx = 1 if confidence > 0.5 else 0
        predicted_class = class_names[predicted_class_idx]
        if predicted_class_idx == 0:
            confidence = 1 - confidence
    return predicted_class, confidence, predictions[0]
