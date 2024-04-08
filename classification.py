
import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

def animal_classification():
    model = tf.keras.models.load_model('data/1.h5') 
    class_labels = ["Least Concern", "Near Threatened", "Vulnerable","Endangered", ...] 
    def preprocess_image(image):
        img = image.resize((299, 299)) 
        img = img.convert('RGB') 
        img = np.array(img)
        img = img / 255.0
        img = np.expand_dims(img, axis=0)
        return img

    def predict(image):
        processed_image = preprocess_image(image)
        prediction = model.predict(processed_image)
        predicted_class = np.argmax(prediction)
        st.write(class_labels[predicted_class],   "Animal      , " , prediction[0][predicted_class])
        return prediction

    st.title('Image Classifier')
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Classifying...")

        prediction = predict(image)

        st.write("Prediction:")
        st.write(prediction)

# animal_classification()
