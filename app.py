
from random import choice
from d import video1
from test import home_page, login_or_signup, survey_form
import explore, upload, counting
from streamlit_option_menu import option_menu

from io import StringIO
import streamlit as st
from classification import animal_classification
from counting import animal_counting

from upload import uploads
from information import animal_information, robo, robo1, robo2
from explore import display_image, explore, viewer
import pandas as pd
from streamlit_option_menu import option_menu
import numpy as np

from PIL import Image
import account
import streamlit.components.v1 as components


def display_homepage():
    """

    Display homepage with a compelling slogan and introduction.
    """

    st.image("data/elephant-48423.svg", use_column_width=True)  # Add an attractive wildlife image
    st.markdown("<h1 style='text-align: lcenter; color: green;'>Wildlife Conservation</h1>", unsafe_allow_html=True)

    video_file = open('data/1.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)
    st.markdown("<h3 style='text-align: center;'>Join hands in making the world a sanctuary for wildlife.</h3>", unsafe_allow_html=True)

    st.write("""
 

Welcome to our Wildlife Conservation Web Application.
               We're using state-of-the-art technology to drive the mission of Wildlife Conservation.

 
🌿Count with Precision: Our tech doesn't just count animals; it spotlights each one uniquely. 🐾✨
Computer do the Tagging

🔍Classify, Track, Preserve: Beyond counting, this project also classifies and tracks, capturing the essence of conservation. An interface where nature and technology dance in harmony. 🌿🤖
             
             
Anyone collecting camera trap photos can upload them to Wildlife Project. Photos are stored online so you can access them from anywhere, from any device or computer, even out in the field.

Animals in your photos are automatically identified using machine learning technology. Thousands of images can be tagged within minutes, saving you time to do the important work.

    """)
    
st.button('Rerun')

def main():
    # st.title("Wildlife Conservation")
    st.sidebar.title("")

    with st.sidebar:        
        app = option_menu(
            menu_title='Wildlife Conservation',
            options=['Home','Account','Survey Form','Data Visualization','Upload Images','Video Detection','Animal Classification','Animal Information',],
            icons=['house-fill','chart-line','cloud-upload','person-badge','grid','info-circle'],
            menu_icon='chat-text-fill',
            default_index=0,
            styles={
                "container": {"padding": "5px","background-color":''},
                "icon": {"color": "black", "font-size": "23px"}, 
                "nav-link": {"color":"black","font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "Green"},
                "nav-link-selected": {"background-color": "#02ab21"},
            }
        )

    if app == "Home":
        display_homepage()
    elif app == "Account":
        if 'authenticated' not in st.session_state:
            st.session_state['authenticated'] = False
        if not st.session_state['authenticated']:
            login_or_signup()
        else:
            st.success("You are logged in. Navigate to other pages.")
    elif app == "Survey Form":
        if st.session_state.get('authenticated', False):
            survey_form()
        else:
            st.warning("Please login to fill out the survey.")
    elif app == "Data Visualization":
        viewer()

    elif app == "Upload Images":
        uploads()

    elif app == "Video Detection":
        video1()

    elif app == "Animal Information":
        animal_classification()

    elif app == "Animal Classification":
        robo2()
        animal_information()
    


    
    st.image("data/Identify.png", use_column_width=True) 

    paragraph = """
    We urgently need to understand the presence and absence of species and their population trends in the areas where we work. Camera trap surveys are an effective method for doing this, but each camera trap survey produces tens of thousands of images, all of which need to be looked at. 
    but this can involve weeks or even months of painstaking effort. To speed up this process, this web application is crowd-sourcing the identifications through our Instant Wild App. Another method that has huge potential to transform our work is automated image recognition, using the power of machine learning to complete large scale species recognition within images.   
    By using the essentially limitless processing power of computers to do the hard work of identifying species within images, we can dramatically speed up the analysis of camera trap surveys and monitor wildlife trends in near real time. 


    """


    paraQ = """
    Is the image empty? 

    Is there a human in the image? 

    What species group (i.e. Animal or  bird) are present in the image? 

    What specific species are present in the image? 

    How many animals are present in the image? 

    """

    paraC = """


    ⦿ Expertise needed for training and testing algorithms. 

    ⦿ Availability of large, manually identified training datasets.

    ⦿ Complex data preparation requirements.

    ⦿ Barriers for implementing algorithms in the field.

    ⦿ Limited adoption due to complexity and accessibility issues.

    """






    st.markdown("<h2 style='text-align: center;'>Why is machine learning important for  wildlife conservation?</h2>", unsafe_allow_html=True)
    st.write(paragraph)


    st.markdown("<h2 style='text-align: center;'>Key questions of focus include: </h2>", unsafe_allow_html=True)


    st.write(paraQ)


    st.markdown("<h2 style='text-align: center;'>Challenges of machine learning in wildlife conservation:</h2>", unsafe_allow_html=True)

    st.write(paraC)


if __name__ == "__main__":
    main()



st.image("data/9.png", use_column_width=True)  


st.write("-------")
st.write("## Wildlife Conservation ML Project")
st.write("Keep in touch with us")
st.write("Sign up for wildlife updates and ways to get involved") 
st.button("SIGN UP")

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
if 'survey_completed' not in st.session_state:
    st.session_state['survey_completed'] = False

if not st.session_state['authenticated']:
    login_or_signup()
elif st.session_state['authenticated'] and not st.session_state['survey_completed']:
    survey_form()
else:
    home_page()
st.write("### Guided by : Dr. Mahendra B. Salunke ")
st.write("###### Developed by: Group No. 9")
st.write("- ###### Vedant Angane")
st.write("- ###### Manvi Gawande")
st.write("- ###### Vaidahi Pawar")
st.write("- ###### Gaurav Suryavanshi")


st.write("#### Copyright © 2024. All rights reserved.")

st.write("---")



