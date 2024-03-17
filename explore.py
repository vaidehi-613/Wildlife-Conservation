import streamlit as st



import streamlit as st

def main():
    st.title("Grid of Buttons")

    # Define the grid layout
    col1, col2, col3 = st.columns(3)

    # Define buttons for each column
    with col1:
        if st.button("Button 1"):
            st.write("You clicked Button 1!")
    with col2:
        if st.button("Button 2"):
            st.write("You clicked Button 2!")
    with col3:
        if st.button("Button 3"):
            st.write("You clicked Button 3!")

    col4, col5, col6 = st.columns(3)

    with col4:
        if st.button("Button 4"):
            st.write("You clicked Button 4!")
    with col5:
        if st.button("Button 5"):
            st.write("You clicked Button 5!")
    with col6:
        if st.button("Button 6"):
            st.write("You clicked Button 6!")

if __name__ == "__main__":
    main()


# import streamlit as st

# # Page Configuration
# st.set_page_config(page_title="Visualization Concept", layout="wide")

# # Main Header
# st.title("Visualization Concept")

# # Main Box: Visualization
# st.header("Visualization")

# # Create a tree-like structure using expander widgets

# # Expander for Stats
# with st.expander("Stats"):
#     st.markdown("Display key statistical metrics with engaging visuals:")
#     st.image("1.jpg")  # Placeholder for a statistical visualization


# def run():
#     embedded_html = """
#     <div class='tableauPlaceholder' id='viz1708270298125' style='position: relative'><noscript><a href='#'><img alt='Reptiles Found in India ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Re&#47;ReptilesfoundinIndia&#47;Sheet1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='ReptilesfoundinIndia&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Re&#47;ReptilesfoundinIndia&#47;Sheet1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-GB' /></object></div>
#     <script type='text/javascript'>var divElement = document.getElementById('viz1708270298125');var vizElement = divElement.getElementsByTagName('object')[0];vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';var scriptElement = document.createElement('script');scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';vizElement.parentNode.insertBefore(scriptElement, vizElement);</script>
#     """

#     st.components.v1.html(embedded_html, height=700)

# run()




def explore():

    st.subheader("Upload an animal image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
        st.write("Classifying...")

        # Ideally, here you'd use a model like ResNet or VGG for classification
        # status = classify_animal(uploaded_file)
        # Mocking the result for now
        st.write("This animal is:", "Endangered")  # Mock classification

from prettymapp.geo import get_aoi
from prettymapp.osm import get_osm_geometries
from prettymapp.plotting import Plot
from prettymapp.settings import STYLES

aoi = get_aoi(address="Praça Ferreira do Amaral, Macau", radius=1100, rectangular=False)
df = get_osm_geometries(aoi=aoi)

fig = Plot(
    df=df,
    aoi_bounds=aoi.bounds,
    draw_settings=STYLES["Peach"]
).plot_all()

fig.savefig("map.jpg")