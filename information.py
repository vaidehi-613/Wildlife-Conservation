import streamlit as st
import pandas as pd

# Load the dataset
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
    if st.checkbox('Show the entire dataset',key='1'):
     st.dataframe(animal_data)

    """
    Display the animal information from the dataset with enhanced visual presentation.
    """
    st.subheader("Enter the name of the animal:")
    # Add a unique key parameter to the text_input widget
    user_input = st.text_input("", "", key="animal_search_input").strip().lower()
    
    if user_input:
        # Filter dataset for matches
        matches = animal_data[animal_data['Animal'].str.lower().str.contains(user_input)]['Animal'].unique()
        
        if len(matches) > 0:
            # If there are matches, show them in a dropdown for the user to select
          selected_animal = st.selectbox("Select an animal:", matches, key="animal_select_box")
          info = fetch_animal_info_from_dataset(selected_animal)
            
          if info is not None:
            # Display the animal information
            # image_url = info.get('Image_URL', 'https://placekitten.com/200/200')  # Placeholder image
            # st.image(image_url, use_column_width=True)
            
            # Convert numerical values to string before concatenating
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
            
# Add a checkbox to toggle the display of the dataset

# Call the main function to display the UI
animal_information()
