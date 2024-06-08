# text.py

import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore, auth
from firebase_admin.exceptions import FirebaseError

# Initialize Firebase Admin SDK
def init_firebase():
    cred_path = 'wildlife-comprehension-75d27ea2fd6b.json'
    if not firebase_admin._apps:
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
    else:
        firebase_admin.get_app()

init_firebase()

# Firestore database instance
db = firestore.client()

def login_or_signup():
    st.title('Welcome to Wildlife Conservation App!')
    choice = st.radio('Do you want to Login or Sign Up?', ('Login', 'Sign Up'))

    email = st.text_input('Email Address')
    password = st.text_input('Password', type='password')

    if choice == 'Login':
        if st.button('Login'):
            try:
                user = auth.get_user_by_email(email)
                st.session_state['authenticated'] = True
                st.experimental_rerun()
            except FirebaseError as e:
                st.error('Login Failed: ' + str(e))
    
    elif choice == 'Sign Up':
        if st.button('Create my Account'):
            try:
                user = auth.create_user(email=email, password=password)
                st.success('Account created Successfully! Please Login.')
                st.experimental_rerun()
            except FirebaseError as e:
                st.error('Failed to create account: ' + str(e))

def survey_form():
    st.title('Survey Form')

    question1 = st.text_input("Please enter your first and last name:", key=1)
    question2 = st.text_input("Please enter the email address you used for sign up:", key=2)
    question3 = st.text_input("Your affiliation/organization:", key=3)
    question4 = st.selectbox("Organization type:", ["Government", "Academia", "Non Profit", "Commercial", "Other"])
    question5 = st.text_area("Describe your project:")
    question6 = st.text_input("In what countries have you collected camera trap data?", key=6)
    files = st.file_uploader("Upload Photos", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    if st.button("Submit"):
        doc_ref = db.collection(u'survey_responses').add({
            u'question1': question1, u'question2': question2, u'question3': question3,
            u'question4': question4, u'question5': question5, u'question6': question6
        })
        st.success("Survey submitted successfully!")
        st.session_state['survey_completed'] = True
        st.experimental_rerun()

def home_page():
    st.title("Home Page")
    st.write("Welcome to the home page!")

def sign():
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

if __name__ == '__main__':
    sign()
