# import base64
# import streamlit as st
# import pandas as pd

# from classification import display_text_result, perform_inference

# import streamlit as st


# import streamlit as st
# import requests
# from io import BytesIO
# from PIL import Image
# import base64
# import json



from inference_sdk import InferenceHTTPClient

# # CLIENT = InferenceHTTPClient(
# #     api_url="https://detect.roboflow.com",
# #     api_key="coZNWQb0K35yZfbOU3rf"
# # )
# # file1 = st.file_uploader("Upload File")
# # result = CLIENT.infer(file1, model_id="animal-detection-jvsw5/1")
# # from roboflow import Roboflow

# # rf = Roboflow(api_key="vlmLfp4rGVbfbzmqp8zx")
# # project = rf.workspace().project("animal-detection-jvsw5")
# # model = project.version("1").model

# # job_id, signed_url, expire_time = model.predict_video(
# #     "Trail Cam Videos_ 1000 Hours in the Jungle_ Rain Forest Animals Puma.mp4",
# #     fps=5,
# #     prediction_type="batch-video",
# # )

# # results = model.poll_until_video_results(job_id)

# # print(results)
# # import streamlit as st
# # import streamlit as st
# # from inference_sdk import InferenceHTTPClient
# # import base64

# # import base64
# # # from roboflow import InferenceHTTPClient
# # import streamlit as st



import time
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

from io import BytesIO
from PIL import Image
import base64

import streamlit as st
import streamlit as st
# from inference_sdk import InferenceHTTPClient
import base64
import pandas as pd

import base64
import streamlit as st

from inference_sdk import InferenceHTTPClient

def display_text_result(result):
    time_taken = result.get("time")
    image_width = result.get("image", {}).get("width")
    image_height = result.get("image", {}).get("height")
    predictions = result.get("predictions", [])
    animal_names = [prediction.get('class') for prediction in predictions]

    st.write("#### Detected Animals List :")

    for i, animal_name in enumerate(animal_names, start=1):
        st.write(f"#### Animal {i}:  {animal_name}")
    # for i in range(5):
    #     if st.checkbox("", key=f'uniqueKey{i+4}', value=False):
    #         pass
    st.write("All detected animals:", ", ".join(animal_names))

    result_text = f"Inference Time: {time_taken} seconds \n \n Image Width: {image_width}, Image Height: {image_height}\n"
    for i, prediction in enumerate(predictions, start=1):
        result_text += (f"\nPrediction {i}:\n"
                        f"Class: {prediction.get('class')}\n \n"
                        f"Confidence: {prediction.get('confidence')}\n"
                        f"\nPosition: (x: {prediction.get('x')}, y: {prediction.get('y')})\n"
                        f"\nSize: (width: {prediction.get('width')}, height: {prediction.get('height')})\n")

    st.write(result_text)
    return animal_names

# def robo():
#     st.title("Image Inference")
#     detected_animals = display_text_result(result)  # This will return the list of animal names
#     for animal in detected_animals:
#       st.markdown(f"### Information for {animal.capitalize()}:")
#       animal_info = fetch_animal_info_from_dataset(animal)
#       if animal_info is not None and not animal_info.empty:
#         st.markdown("**Height:** " + str(animal_info['Height (cm)']))
#         st.markdown("**Weight:** " + str(animal_info['Weight (kg)']))
#         st.markdown("**Color:** " + animal_info['Color'])
#         st.markdown("**Lifespan:** " + str(animal_info['Lifespan (years)']))
        
#         st.write("Diet:", animal_info['Diet'])
#         st.write("Habitat:", animal_info['Habitat'])
#         st.write("Predators:", animal_info['Predators'])
#         st.write("Average Speed (km/h):", str(animal_info['Average Speed (km/h)']))
#         st.write("Countries Found:", animal_info['Countries Found'])
        
#         st.write("Conservation Status:")
#         display_conservation_status(animal_info['Conservation Status'])
#         st.write("Family:", animal_info['Family'])
#         st.write("Gestation Period (days):", str(animal_info['Gestation Period (days)']))
#         st.write("Top Speed (km/h):", str(animal_info['Top Speed (km/h)']))
#         st.write("Social Structure:", animal_info['Social Structure'])
#         st.write("Offspring per Birth:", str(animal_info['Offspring per Birth']))
#       else:
#         st.write("No information found for this animal.")

#     """
# Discover detailed insights about animals with our enhanced visual presentation feature. Dive into our comprehensive dataset to learn more about your favorite animals, displayed in a visually appealing format.

# """    
#     if st.checkbox('Show the entire dataset',key='1234'):
#       st.dataframe(animal_data)
#     CLIENT = InferenceHTTPClient(
#         api_url="https://detect.roboflow.com",
#         api_key="coZNWQb0K35yZfbOU3rf"
#     )

#     uploaded_file = st.file_uploader("Choose a file")

#     if uploaded_file is not None:
#         st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
#         st.markdown("<h3 style='text-align: left; color: black;'>Classifying...</h3>", unsafe_allow_html=True)

#         # Create a progress bar instance
#         progress_bar = st.progress(0)

#         # Time duration for the progress bar to fill
#         duration = 5  # duration in seconds
#         increments = 20  # increase the progress bar in 5% increments
#         percent_complete = st.empty()


#         for i in range(increments + 1):
#             # Update progress bar by increment

#             progress = int(100 * i / increments)
#             progress_bar.progress(progress)
#             percent_complete.text(f"Progress: {progress}%")
#             # Wait a bit before the next update
#             time.sleep(duration / increments)

#         image_bytes = uploaded_file.read()

#         image_base64 = base64.b64encode(image_bytes).decode("utf-8")

#         result = CLIENT.infer(image_base64, model_id="animal-detection-jvsw5/1")

#         st.write("Inference result:")
#         display_text_result(result)


import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import requests
from io import BytesIO

# Load the InceptionV3 model pre-trained on ImageNet
model = tf.keras.applications.InceptionV3(weights='imagenet')

# Preprocess the image
def preprocess_image(image):
    image = image.resize((299, 299))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = tf.keras.applications.inception_v3.preprocess_input(image)
    return image

# Decode predictions to get human-readable labels
def decode_predictions(predictions):
    labels = tf.keras.applications.inception_v3.decode_predictions(predictions, top=5)[0]
    return labels
    st.title("Animal Classifier using InceptionV3")
    upload_method = st.radio("Upload Method", ["Upload", "URL"])
    if upload_method == "Upload":
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
    else:
        url = st.text_input("Image URL")
        if url:
            response = requests.get(url)
            image = Image.open(BytesIO(response.content))
    classes = st.text_input("Filter Classes (comma separated)", value="")
    confidence = st.slider("Min Confidence", min_value=0, max_value=100, value=40)
    overlap = st.slider("Max Overlap", min_value=0, max_value=100, value=30)
    format = st.radio("Inference Result", ["Image", "JSON"])

    if (upload_method == "Upload" and uploaded_file is not None) or (upload_method == "URL" and url):
        st.image(image, caption="Uploaded Image", use_column_width=True)
        image = preprocess_image(image)
        predictions = model.predict(image)
        labels = decode_predictions(predictions)
        
        if format == "Image":
            st.header("Top Predictions")
            for label in labels:
                st.write(f"{label[1]}: {label[2] * 100:.2f}%")
        else:
            st.header("Predictions in JSON format")
            st.json([{label[1]: label[2] * 100} for label in labels])



animal_data = pd.read_csv('data/AnimalDataset.csv')

def fetch_animal_info_from_dataset(animal_name):
    """
    Fetch animal information from the provided dataset for names up to three words long.
    """
    animal_name = animal_name.lower().strip().split()
    if len(animal_name) == 1:
        info = animal_data[animal_data['Animal'].str.lower() == animal_name[0]].squeeze()
    else:
        search_query = " ".join(animal_name)  # Re-join for exact match in case of multi-word names
        info = animal_data[animal_data['Animal'].str.lower() == search_query].squeeze()
    return info if not info.empty else None

def display_conservation_status(status):
    """
    Display conservation status with color coding.
    """


    status_colors = {

        'Least Concern': 'green',

        'Vulnerable': 'orange',

        'Endangered': 'red',

        'Critically Endangered': 'darkred'

    }

    color = status_colors.get(status, 'blue')
    st.markdown(f"<div style='color: {color}; font-size: 24px;'>{status}</div>", unsafe_allow_html=True)

def animal_information():
    
    user_input = st.text_input("", "", key="animal_search_input").strip().lower()
    
    if user_input:
        matches = animal_data[animal_data['Animal'].str.lower().str.contains(user_input)]['Animal'].unique()
        
        if len(matches) > 0:
          selected_animal = st.selectbox("Select an animal:", matches, key="animal_select_box")
          info = fetch_animal_info_from_dataset(selected_animal)
            
          if info is not None:
            st.markdown("**Height:** " + str(info['Height (cm)']))
            st.markdown("**Weight:** " + str(info['Weight (kg)']))
            st.markdown("**Color:** " + info['Color'])
            st.markdown("**Lifespan:** " + str(info['Lifespan (years)']))
            
            st.write("Diet:", info['Diet'])
            st.write("Habitat:", info['Habitat'])
            st.write("Predators:", info['Predators'])
            st.write("Average Speed (km/h):", str(info['Average Speed (km/h)']))
            st.write("Countries Found:", info['Countries Found'])
            
            st.write("Conservation Status:")
            display_conservation_status(info['Conservation Status'])
            
            st.write("Family:", info['Family'])
            st.write("Gestation Period (days):", str(info['Gestation Period (days)']))
            st.write("Top Speed (km/h):", str(info['Top Speed (km/h)']))
            st.write("Social Structure:", info['Social Structure'])
            st.write("Offspring per Birth:", str(info['Offspring per Birth']))
          else:
            st.write("No information found for this animal.")
            
import streamlit as st
import requests
import base64
import time



def call_api(model, version, api_key, file=None, url=None, classes=None, confidence=50, overlap=50, format="json"):
    api_url = f"https://detect.roboflow.com/{model}/{version}"
    params = {
        
        'api_key': api_key,
        'confidence': confidence / 100,
        'overlap': overlap / 100,
        'format': format
    }
    if classes:
        params['classes'] = classes
    
    if file:
        files = {'file': file}
        response = requests.post(api_url, params=params, files=files)
    elif url:
        params['image'] = url
        response = requests.post(api_url, params=params)
    else:
        return None

    return response


def robo2():
    st.title("Animal Detection and Species Profile")
 
    if st.checkbox('Show the entire dataset', key='12334'):
        st.dataframe(animal_data)

    # uploaded_file = st.file_uploader("Choose a file")

    # if uploaded_file is not None:
    #     st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
    #     st.markdown("<h5 style='text-align: left; color: black;'>Classifying...</h5>", unsafe_allow_html=True)
        
    colors = [
        "#cefa", "#abf7b1", "#83f28f", "#5ced73", 
        "#39e75f", "#1fd655", "#00c04b", 
        "#00ab41", "#008631"
    ]
    
    # container = st.container()
    # progress_text = container.empty()
    # my_bar = st.progress(0)

    # progress_text.markdown("<h3 style='text-align: center; color: black;'>Operation is Completed. Please wait.</h3>", unsafe_allow_html=True)

    # duration = 5
    # increments = 100

    # for i in range(increments + 1):
    #     percent_complete = int(100 * i / increments)
    #     if i == 101:
    #         st.markdown("<h5 style='text-align: left; color: black;'>Performing Classfication on Image that yoou provided...</h5>", unsafe_allow_html=True)

    #     color_index = min(len(colors) - 1, percent_complete // (100 // len(colors)))
    #     color = colors[color_index]

    #     my_bar.progress(percent_complete)
    #     progress_text.markdown(f"<h3 style='text-align: center; color: {color};'>{percent_complete}% - Operation Completed</h3>", unsafe_allow_html=True)
    #     time.sleep(duration / increments)

    model = "animal-detection-jvsw5"
    version = 1
    api_key = "vlmLfp4rGVbfbzmqp8zx"

    upload_method = st.radio("Upload Method", ["Upload", "URL"])
    if upload_method == "Upload":
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    else:
        url = st.text_input("Image URL")

    # classes = st.text_input("Filter Classes (comma separated)")
    # confidence = st.slider("Min Confidence", min_value=0, max_value=100, value=40)
    # overlap = st.slider("Max Overlap", min_value=0, max_value=100, value=30)
    # format = st.radio("Inference Result", ["Image", "JSON"])

    classes = "class1,class2,class3"  # Comma-separated list of classes to filter
    confidence = 40  # Minimum confidence level (0 to 100)
    overlap = 30  # Maximum overlap (0 to 100)
    format = "JSON"  # Options: "Image", "JSON"

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
        

        if upload_method == "Upload":
            response = call_api(model, version, api_key, file=uploaded_file, classes=classes, confidence=confidence, overlap=overlap, format=format.lower())
            message_placeholder = st.empty()
            message_placeholder.markdown("<h5 style='text-align: left; color: red;'>Classifying...</h5>", unsafe_allow_html=True)
            time.sleep(4)
            message_placeholder.empty()
        elif upload_method == "URL" and url:
            response = call_api(model, version, api_key, url=url, classes=classes, confidence=confidence, overlap=overlap, format=format.lower())
        else:
            st.error("Please provide an image file or URL.")
            response = None
        
        if response:
            st.markdown("<h5 style='text-align: left; color: Green;'>Classification Done...</h5>", unsafe_allow_html=True)
            if response.status_code == 200:
                data = response.json()
                detected_animals = display_text_result(data)
                st.write(detected_animals[0])


                for index, animal in enumerate(detected_animals):
                    user_input = animal
                    if user_input:
                        matches = animal_data[animal_data['Animal'].str.lower().str.contains(user_input)]['Animal'].unique()

                        if len(matches) > 0:
                            key = f"animal_select_box_{index}"
                            selected_animal = st.selectbox("Select an animal:", matches, key=key)
                            info = fetch_animal_info_from_dataset(selected_animal)

                            if info is not None:
                                st.markdown("**Height:** " + str(info['Height (cm)']))
                                st.markdown("**Weight:** " + str(info['Weight (kg)']))
                                st.markdown("**Color:** " + info['Color'])
                                st.markdown("**Lifespan:** " + str(info['Lifespan (years)']))
                                st.write("Diet:", info['Diet'])
                                st.write("Habitat:", info['Habitat'])
                                st.write("Predators:", info['Predators'])
                                st.write("Average Speed (km/h):", str(info['Average Speed (km/h)']))
                                st.write("Countries Found:", info['Countries Found'])
                                st.write("Conservation Status:")
                                display_conservation_status(info['Conservation Status'])
                                st.write("Family:", info['Family'])
                                st.write("Gestation Period (days):", str(info['Gestation Period (days)']))
                                st.write("Top Speed (km/h):", str(info['Top Speed (km/h)']))
                                st.write("Social Structure:", info['Social Structure'])
                                st.write("Offspring per Birth:", str(info['Offspring per Birth']))
                            else:
                                st.write("No information found for this animal.")
            else:
                st.error(f"Error: {response.status_code}")
                st.error(response.text)
        else:
            st.write("Please upload an animal image to start the process.")



def robo1():
    st.title("Animal Detection and Species Profile")
 
    if st.checkbox('Show the entire dataset', key='1234'):
        st.dataframe(animal_data)

    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
        st.markdown("<h5 style='text-align: left; color: black;'>Classifying...</h5>", unsafe_allow_html=True)
        
        colors = [
            "#cefa", "#abf7b1", "#83f28f", "#5ced73", 
            "#39e75f", "#1fd655", "#00c04b", 
            "#00ab41", "#008631"
        ]
        
        container = st.container()
        progress_text = container.empty()
        my_bar = st.progress(0)

        progress_text.markdown("<h3 style='text-align: center; color: black;'>Operation is Completed. Please wait.</h3>", unsafe_allow_html=True)

        duration = 5
        increments = 100

        for i in range(increments + 1):
            percent_complete = int(100 * i / increments)
            if i == 101:
                st.markdown("<h5 style='text-align: left; color: black;'>Performing inference...</h5>", unsafe_allow_html=True)

            color_index = min(len(colors) - 1, percent_complete // (100 // len(colors)))
            color = colors[color_index]

            my_bar.progress(percent_complete)
            progress_text.markdown(f"<h3 style='text-align: center; color: {color};'>{percent_complete}% - Operation is...</h3>", unsafe_allow_html=True)
            time.sleep(duration / increments)

        image_bytes = uploaded_file.read()
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")
        
        api_url = "https://detect.roboflow.com/animal-detection-jvsw5/1"
        api_key = "coZNWQb0K35yZfbOU3rf"

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }


        data = {
            "image": image_base64
        }

        response = requests.post(api_url, headers=headers, json=data)
        st.write(response)
        if response.status_code == 200:
            result = response.json()
            detected_animals = display_text_result(result)
            st.write(detected_animals[0])

            for index, animal in enumerate(detected_animals):
                user_input = animal
                if user_input:
                    matches = animal_data[animal_data['Animal'].str.lower().str.contains(user_input)]['Animal'].unique()

                    if len(matches) > 0:
                        key = f"animal_select_box_{index}"
                        selected_animal = st.selectbox("Select an animal:", matches, key=key)
                        info = fetch_animal_info_from_dataset(selected_animal)

                        if info is not None:
                            st.markdown("**Height:** " + str(info['Height (cm)']))
                            st.markdown("**Weight:** " + str(info['Weight (kg)']))
                            st.markdown("**Color:** " + info['Color'])
                            st.markdown("**Lifespan:** " + str(info['Lifespan (years)']))
                            st.write("Diet:", info['Diet'])
                            st.write("Habitat:", info['Habitat'])
                            st.write("Predators:", info['Predators'])
                            st.write("Average Speed (km/h):", str(info['Average Speed (km/h)']))
                            st.write("Countries Found:", info['Countries Found'])
                            st.write("Conservation Status:")
                            display_conservation_status(info['Conservation Status'])
                            st.write("Family:", info['Family'])
                            st.write("Gestation Period (days):", str(info['Gestation Period (days)']))
                            st.write("Top Speed (km/h):", str(info['Top Speed (km/h)']))
                            st.write("Social Structure:", info['Social Structure'])
                            st.write("Offspring per Birth:", str(info['Offspring per Birth']))
                        else:
                            st.write("No information found for this animal.")
        else:
            st.write("Error:", response.status_code, response.text)

    else:
        st.write("Please upload an animal image to start the process.")


def robo():
    st.title("Animal Detection and Species Profile")
 
    if st.checkbox('Show the entire dataset', key='1234'):
        st.dataframe(animal_data)
    
    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key="coZNWQb0K35yZfbOU3rf",

    )

    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True,)
        st.markdown("<h5 style='text-align: left; color: black;'>Classifying...</h3>", unsafe_allow_html=True)
        st.write()
        st.write()

        
        colors = [
    "#cefa",  # assuming the correct color code should have two additional characters
    "#abf7b1", "#83f28f", "#5ced73", 
    "#39e75f", "#1fd655", "#00c04b", 
    "#00ab41", "#008631"
]
        # Create a container for better control over layout
        container = st.container()
        progress_text = container.empty()  # Placeholder for displaying progress text
        my_bar = st.progress(0)            # Initial progress bar setup

        # Display initial operation message
        progress_text.markdown("<h3 style='text-align: center; color: black;'>Operation is Completed. Please wait.</h3>", unsafe_allow_html=True)

        # Time duration for the progress bar to fill
        duration = 5  # duration in seconds
        increments = 100  # increment for finer progress control

        for i in range(increments + 1):
            # Calculate progress percentage
            percent_complete = int(100 * i / increments)
            if i==101:
                st.markdown("<h5 style='text-align: left; color: black;'>Performing inference...</h3>", unsafe_allow_html=True)

            # Determine color based on progress
            color_index = min(len(colors) - 1, percent_complete // (100 // len(colors)))  # Ensure index is within range
            color = colors[color_index]

            # Update progress bar and text with color
            my_bar.progress(percent_complete)
            progress_text.markdown(f"<h3 style='text-align: center; color: {color};'>{percent_complete}% - Operation is...</h3>", unsafe_allow_html=True)
            
            # Pause briefly
            time.sleep(duration / increments)

       
            
        image_bytes = uploaded_file.read()
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")
        
        result = CLIENT.infer(image_base64, model_id="animal-detection-jvsw5/1")
        # st.write("### Inference result:")
        
        detected_animals = display_text_result(result)  # Ensures result is defined before use
        st.write(detected_animals[0])
        i=0
        for index, animal in enumerate(detected_animals):
            user_input = animal
            if user_input:
                matches = animal_data[animal_data['Animal'].str.lower().str.contains(user_input)]['Animal'].unique()
                
                if len(matches) > 0:
                    key = f"animal_select_box_{index}"  # Unique key based on index
                    selected_animal = st.selectbox("Select an animal:", matches, key=key)
                info = fetch_animal_info_from_dataset(selected_animal)
                    
                if info is not None:
                    st.markdown("**Height:** " + str(info['Height (cm)']))
                    st.markdown("**Weight:** " + str(info['Weight (kg)']))
                    st.markdown("**Color:** " + info['Color'])
                    st.markdown("**Lifespan:** " + str(info['Lifespan (years)']))
                    
                    st.write("Diet:", info['Diet'])
                    st.write("Habitat:", info['Habitat'])
                    st.write("Predators:", info['Predators'])
                    st.write("Average Speed (km/h):", str(info['Average Speed (km/h)']))
                    st.write("Countries Found:", info['Countries Found'])
                    
                    st.write("Conservation Status:")
                    display_conservation_status(info['Conservation Status'])
                    
                    st.write("Family:", info['Family'])
                    st.write("Gestation Period (days):", str(info['Gestation Period (days)']))
                    st.write("Top Speed (km/h):", str(info['Top Speed (km/h)']))
                    st.write("Social Structure:", info['Social Structure'])
                    st.write("Offspring per Birth:", str(info['Offspring per Birth']))
                else:
                    st.write("No information found for this animal.")

           
    else:
            st.write("Please upload an animal image to start the process.")


# Ensure to call robo() function at the appropriate place in your script
# robo()

