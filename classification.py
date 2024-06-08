
import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

import streamlit as st


import streamlit as st
import requests
from io import BytesIO
from PIL import Image
import base64
import json


import streamlit as st
import streamlit as st
import base64

import base64
import streamlit as st

import pandas as pd

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

def animal_classification():
    st.write("""### Explore the realm of wildlife conservation with our ML-driven insights. 
             
             
             
Empowering Wildlife Conservation Through Advanced Machine Learning: Classify, Understand, and Actively Contribute to Protecting Biodiversity.
    
Explore the realm of wildlife conservation with our ML-driven insights. Get to know the animals that inhabit our world and understand the efforts to conserve them, all through an engaging visual interface.

##### Quick Start:
1. **Identify an Animal**: Enter the name of an animal to receive tailored conservation status, habitat information, and threats facing the species.


             """)
    
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

def perform_inference(model, version, api_key, upload_method, file, url, filter_classes, min_confidence, max_overlap, inference_result):
    settings = {
        "method": "POST",
    }

    parts = [
        "https://detect.roboflow.com/",
        model,
        "/",
        str(version),
        "?api_key=" + api_key
    ]
    
    if filter_classes:
        parts.append("&classes=" + filter_classes)

    if min_confidence:
        parts.append("&confidence=" + str(min_confidence))

    if max_overlap:
        parts.append("&overlap=" + str(max_overlap))

    format_val = inference_result.lower()
    parts.append("&format=" + format_val)
    settings["format"] = format_val

    stroke_width = st.radio("Stroke Width", ("1px", "2px", "5px", "10px"), key="stroke_width_radio")
    show_labels = st.radio("Labels", ("Off", "On"), key="show_labels_radio")

    labels = "on" if show_labels == "On" else "off"
    parts.append("&labels=" + labels)

    if stroke_width:
        parts.append("&stroke=" + stroke_width.replace("px", ""))

    def override_xhr():
        override = requests.post(settings["url"])
        override.responseType = 'arraybuffer'
        return override

    settings["xhr"] = override_xhr

    method = "upload" if upload_method == "Upload" else "url"
    parts.append("&method=" + method)

    if method == "upload":
        if not file:
            st.error("Please select a file.")
            return

        base64image = base64.b64encode(file.read()).decode("utf-8")
        settings["data"] = base64image
    else:
        if not url:
            st.error("Please enter an image URL.")
            return

        parts.append("&image=" + url)

    settings["url"] = "".join(parts)

    try:
        response = requests.post(settings["url"], data=settings.get("data", None))

        if settings["format"] == "json":
            return response.json()
        else:
            img = Image.open(BytesIO(response.content))
            return img

    except Exception as e:
        st.error("Error loading response.\n\nCheck your API key, model, version, and other parameters then try again.")
        st.error(str(e))
        return None
