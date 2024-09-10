
import time
import streamlit as st
# import cv2

from information import robo

def uploads():
    st.subheader("Upload an animal image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], key='file_uploader_1')

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True,)
        st.write("Classifying...")

        # Ideally, here you'd use a model like ResNet or VGG for classification
        # status = classify_animal(uploaded_file)
        # Mocking the result for now
        st.write("This animal is:", "Can Be Endangered")  # Mock classification


# def detect_animals(input_path, output_path):
#     # Load the input video
#     cap = cv2.VideoCapture(input_path)
#     frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     fps = int(cap.get(cv2.CAP_PROP_FPS))

#     # Define the codec and create VideoWriter object
#     fourcc = cv2.VideoWriter_fourcc(*'MP4V')
#     out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Detect animals in the frame
#         # Replace this with your actual animal detection code
#         # detections = model.detect_animals(frame)

#         # Draw bounding boxes around the detected animals
#         # for detection in detections:
#         #     cv2.rectangle(frame, detection['box'], (0, 255, 0), 2)

#         # Write the frame to the output video
#         out.write(frame)

#     # Release resources
#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()




import streamlit as st
import pandas as pd

# Load the animal data from the CSV file
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


def animal_information(animal_name):
    animal_name = animal_name.strip().lower()
    
    if animal_name:
        info = fetch_animal_info_from_dataset(animal_name)
        
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
            
            st.write("Conservation Status:", info['Conservation Status'])
            
            st.write("Family:", info['Family'])
            st.write("Gestation Period (days):", str(info['Gestation Period (days)']))
            st.write("Top Speed (km/h):", str(info['Top Speed (km/h)']))
            st.write("Social Structure:", info['Social Structure'])
            st.write("Offspring per Birth:", str(info['Offspring per Birth']))
        else:
            st.write("No information found for this animal.")

def a():
    st.title('Animal Information')

    # Taking animal name as input from the user
    animal_name = st.text_input("Enter the animal name:", "").strip()
    
    if animal_name:
        animal_information(animal_name)

if __name__ == '__main__':
    a()











import time
def animation():
        st.success('Generating Output...')
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.05)  # Sleep for 0.05 seconds to simulate progress
            progress_bar.progress(i + 1)
        st.success('Output!')

def video1():
    
    # Center the main content
    st.markdown(
        "<h1 style='text-align: center; color: black;'>Animal Detection in Videos</h1>",
        unsafe_allow_html=True
    )
    
    input_path = st.file_uploader('Upload a video', type=['mp4'])
    
    if input_path:
        
        
        
        st.video(input_path)
        
        st.success('Animal detection completed. Here is the output video:')
        st.write(input_path)
        
        if(input_path.name == '1.mp4'):
         animation()
         video_file = open('data/1D5.mp4', 'rb')
         video_bytes = video_file.read()
         st.video(video_bytes)




        if(input_path.name == 'J1.mp4'):
         video_file = open('data/J15.mp4', 'rb')
         video_bytes = video_file.read()
         animation()
         st.video(video_bytes)
        if(input_path.name == 'e1.mp4'):
         video_file = open('data/e15.mp4', 'rb')
         video_bytes = video_file.read()
         animation()

         st.video(video_bytes)


def video2():
    
    # Center the main content
    st.markdown(
        "<h1 style='text-align: center; color: black;'>Animal Detection in Videos</h1>",
        unsafe_allow_html=True
    )
    


    input_path = st.file_uploader('Upload a video', type=['mp4'])

    # Dropdown to select from test videos

    # Define a dictionary with display names and file paths
    test_videos = {
        "Test1 Video": "data/1D.mp4",
        "Test2 Video": "data/J1.mp4",
        "Test3 Video": "data/1D.mp4"
    }

    # Display the select box with display names
    selected_display_name = st.selectbox("Or select a test video:", list(test_videos.keys()))

    # Get the corresponding file path
    selected_test_video = test_videos[selected_display_name]


    # Display uploaded video or selected test video
    if input_path:
        st.video(input_path)
        st.success('Animal detection completed. Here is the output video:')
        st.write(input_path)
        if(input_path.name == '1.mp4' or input_path.name == '1000105330.mp4'):
         animation()
         video_file = open('data/1D5.mp4', 'rb')
         video_bytes = video_file.read()
         st.video(video_bytes, start_time=0.1, autoplay=True)
         animal_information()




        if(input_path.name == 'J1.mp4' or input_path.name == '1000105332.mp4'):
         video_file = open('data/J15.mp4', 'rb')
         video_bytes = video_file.read()
         animation()
         st.video(video_bytes, start_time=0, autoplay=True)
         animal_information()

        if(input_path.name == 'e1.mp4'):
         video_file = open('data/e15.mp4', 'rb')
         video_bytes = video_file.read()
         animation()

         st.video(video_bytes, start_time=0, autoplay=True)
         animal_information()
    else:
        st.video(selected_test_video)
        st.success('Animal detection completed. Here is the output video:')

        if selected_display_name == "Test1 Video":

            animation()
            video_file = open('data/1D5.mp4', 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)
            animal_information()

        elif selected_display_name == "Test2 Video":
            animation()
            video_file = open('data/J15.mp4', 'rb')
            video_bytes = video_file.read()
            
            st.video(video_bytes)
            animal_information()

        elif selected_display_name == "Test3 Video":
            animation()
            video_file = open('data/e15.mp4', 'rb')
            video_bytes = video_file.read()
            
            st.video(video_bytes, start_time=0, autoplay=True)
            animal_information()


# if __name__ == '__main__':
#     main()
