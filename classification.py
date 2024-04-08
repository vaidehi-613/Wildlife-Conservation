
import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np


def image_classifier():
    model = tf.keras.models.load_model('1.h5') 
    class_labels = ["class1", "class2", "class3", ...] 
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
        st.write(class_labels[predicted_class],   "         " , prediction[0][predicted_class])
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

image_classifier()

# # Load the model and class labels
# model = tf.keras.models.load_model('1.h5')
# class_labels = ["class1", "class2", "class3", ...]  # Replace with your actual class labels

# # # Function to preprocess the image
# # def preprocess_image(image):
# #     img = image.resize((299, 299))
# #     img = img.convert('RGB')
# #     img = np.array(img)
# #     img = img / 255.0
# #     img = np.expand_dims(img, axis=0)
# #     return img

# # # Function to make predictions and return class labels
# # def predict(image):
# #     processed_image = preprocess_image(image)
# #     prediction = model.predict(processed_image)
# #     predicted_class = np.argmax(prediction)
# #     return class_labels[predicted_class], prediction[0][predicted_class]

# # # Streamlit app
# # def main():
# #     st.title('Image Classifier')
# #     uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# #     if uploaded_file is not None:
# #         image = Image.open(uploaded_file)
# #         st.image(image, caption='Uploaded Image.', use_column_width=True)
# #         st.write("")
# #         st.write("Classifying...")

# #         class_name, confidence = predict(image)

# #         st.write("Prediction:")
# #         st.write(f"Class: {class_name}, Confidence: {confidence}")

# # if __name__ == '__main__':
# #     main()

# # Load the model
# # Load the model
# model = tf.keras.models.load_model('1.h5')

# # Function to preprocess the image
# def preprocess_image(image):
#     img = image.resize((299, 299))
#     img = img.convert('RGB')
#     img = np.array(img)
#     img = img / 255.0
#     img = np.expand_dims(img, axis=0)
#     return img

# # Function to make predictions
# def predict(image):
#     processed_image = preprocess_image(image)
#     prediction = model.predict(processed_image)
#     return prediction[0]  # Assuming prediction[0] contains both class and animal name
# # Streamlit app
# # Streamlit app
# # Streamlit app
# # Streamlit app
# def main():
#     # Define animal_names list
#     animal_names = ["animal1", "animal2", "animal3", ...]  # Define your animal names here

#     st.title('Image Classifier')
#     uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

#     if uploaded_file is not None:
#         image = Image.open(uploaded_file)
#         st.image(image, caption='Uploaded Image.', use_column_width=True)
#         st.write("")
#         st.write("Classifying...")

#         prediction = predict(image)

#         # Convert prediction indices to integers
#         class_index = int(prediction[0])
#         animal_name_index = int(prediction[1])

#         # Initialize animal_name variable
#         animal_name = ""

#         # Get class label and animal name based on predicted indices
#         class_label = class_labels[class_index]

#         # Check if animal_name_index is within the range of animal_names
#         if 0 <= animal_name_index < len(animal_names):
#             animal_name = animal_names[animal_name_index]

#         st.write("Prediction:")
#         st.write(f"Class: {class_label}, Animal Name: {animal_name}")

# # if __name__ == '__main__':
# #     main()
# import streamlit as st

# from PIL import Image
# import numpy as np

# def main():
#     st.title("Image Classification with .h5 Model")

#     # Load the model
#     model = tf.keras.models.load_model("1.h5")

#     # File upload
#     uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

#     if uploaded_file is not None:
#         # Display the uploaded image
#         img = Image.open(uploaded_file)
#         st.image(img, caption='Uploaded Image', use_column_width=True)

#         # Preprocess the image
#         img = img.resize((299, 299))  # assuming input size for your model
#         img_array = np.array(img)
#         img_array = img_array[:, :, :3]  # Ensure only 3 channels (RGB)
#         img_array = img_array / 255.0  # normalize pixel values
#         img_array = np.expand_dims(img_array, axis=0)  # add batch dimension

#         # Make predictions
#         predictions = model.predict(img_array)

#         # Display prediction
#         st.write("Predictions:")
#         st.write(predictions)

# if __name__ == "__main__":
#     main()




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
