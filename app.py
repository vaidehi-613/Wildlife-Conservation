from io import StringIO
import streamlit as st
from counting import animal_counting
from classification import animal_classification
from upload import upload
from information import animal_information
from explore import explore
import pandas as pd
import numpy as np
import time

import tableauserverclient as TSC

import streamlit.components.v1 as components

import streamlit as st


def display_homepage():
    """

    Display homepage with a compelling slogan and introduction.
    """
    # st.markdown(
    #      f"""
    #      <style>
    #      .stApp {{
    #          background: url("https://happydays365.org/wp-content/uploads/2019/12/World-Wildlife-Conservation-Day-980x653.jpg");
    #          background-size: cover
    #      }}
    #      </style>
    #      """,
    #      unsafe_allow_html=True
    #  )

    st.image("/home/gaurav/Downloads/elephant-48423.svg", use_column_width=True)  # Add an attractive wildlife image
    st.markdown("<h1 style='text-align: lcenter; color: green;'>Wildlife Conservation</h1>", unsafe_allow_html=True)
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
    
    # with st.status("Downloading data...", expanded=True) as status:
    #     st.write("Searching for data...")
    #     time.sleep(2)

    #     st.write("Found URL.")
    #     time.sleep(1)
    #     st.write("Downloading data...")
    #     time.sleep(1)
    #     status.update(label="Download complete!", state="complete", expanded=False)

st.button('Rerun')






def main():
    st.title("Wildlife Conservation")


    st.sidebar.title("Menu")

    choice = st.sidebar.radio("Select", ["Home","Explore Data","Upload Images", "Animal Counting", "Animal Classification", "Animal Information"])

    if choice == "Home":
        display_homepage()

    elif choice == "Explore Data":
        st.header("Exploe Data Visulaization")
        explore()

    elif choice == "Upload Images":
        st.header("Upload Images")
        upload()

    elif choice == "Animal Information":
        st.header("Animal Information")
        animal_information()
    elif choice == "Animal Counting":
        st.header("Animal Counting")
        animal_counting()

    elif choice == "Animal Classification":
        st.header("Animal Classification")
        animal_classification()

    elif choice == "Animal Information":
        st.header("Animal Information")
        animal_information()

    
    # st.write ("See Map below for the location of the animals")
    # df = pd.DataFrame({
    # "col1": np.random.randn(1000) / 50 + 37.76,
    # "col2": np.random.randn(1000) / 50 + -122.4,
    # "col3": np.random.randn(1000) * 100,
    # "col4": np.random.rand(1000, 4).tolist(),})

    # st.map(df,
    # latitude='col1',
    # longitude='col2',
    # size='col3',
    # color='col4')

if __name__ == "__main__":
    main()

st.image("data/Identify.png", use_column_width=True)  




import streamlit as st
import pandas as pd

data = pd.read_csv('data/animal.csv')



st.markdown("""
            <div class='tableauPlaceholder' id='viz1708268777301' style='position: relative'><noscript><a href='#'><img alt='Reptiles Found in India ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Re&#47;ReptilesinIndia&#47;Sheet1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='ReptilesinIndia&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Re&#47;ReptilesinIndia&#47;Sheet1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-GB' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1708268777301');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
<style>
h1, h2, h3, h4, h5, h6 {
    font-family: 'Soehne', system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif;
}
body {
    font-family: 'Soehne', system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif;
}
</style>
""", unsafe_allow_html=True)

st.title('Animal Population Information')

countries = data['Country'].unique()
selected_country = st.selectbox('Select a Country', countries)

if selected_country:
    st.subheader(f'Animal Population in {selected_country}')
    country_data = data[data['Country'] == selected_country]
    st.write(country_data)


st.image("data/9.png", use_column_width=True)  





# Set up connection.
tableau_auth = TSC.PersonalAccessTokenAuth(
    st.secrets["tableau"]["token_name"],
    st.secrets["tableau"]["token_secret"],
    st.secrets["tableau"]["site_id"],
)
server = TSC.Server(st.secrets["tableau"]["server_url"], use_server_version=True)


# Get various data.
# Explore the tableauserverclient library for more options.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query():
    with server.auth.sign_in(tableau_auth):

        # Get all workbooks.
        workbooks, pagination_item = server.workbooks.get()
        workbooks_names = [w.name for w in workbooks]

        # Get views for first workbook.
        server.workbooks.populate_views(workbooks[0])
        views_names = [v.name for v in workbooks[0].views]

        # Get image & CSV for first view of first workbook.
        view_item = workbooks[0].views[0]
        server.views.populate_image(view_item)
        server.views.populate_csv(view_item)
        view_name = view_item.name
        view_image = view_item.image
        # `view_item.csv` is a list of binary objects, convert to str.
        view_csv = b"".join(view_item.csv).decode("utf-8")

        return workbooks_names, views_names, view_name, view_image, view_csv

workbooks_names, views_names, view_name, view_image, view_csv = run_query()


st.subheader("📊 Data")
st.write(f"And here's the data for view *{view_name}*:")
st.write(pd.read_csv(StringIO(view_csv)))

def run():
    embedded_html = """
    <div class='tableauPlaceholder' id='viz1708270298125' style='position: relative'><noscript><a href='#'><img alt='Reptiles Found in India ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Re&#47;ReptilesfoundinIndia&#47;Sheet1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='ReptilesfoundinIndia&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Re&#47;ReptilesfoundinIndia&#47;Sheet1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-GB' /></object></div>
    <script type='text/javascript'>var divElement = document.getElementById('viz1708270298125');var vizElement = divElement.getElementsByTagName('object')[0];vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';var scriptElement = document.createElement('script');scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';vizElement.parentNode.insertBefore(scriptElement, vizElement);</script>
    """

    st.components.v1.html(embedded_html, height=700)

run()



video_file = open('data/1.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)


# import streamlit as st
# from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
# from htbuilder.units import percent, px
# from htbuilder.funcs import rgba, rgb


# def image(src_as_string, **style):
#     return img(src=src_as_string, style=styles(**style))

# def vimeo_video(video_id):
#     return f'''
#         <iframe src="//player.vimeo.com/video/{video_id}?background=1" 
#                 frameborder="0" 
#                 webkitallowfullscreen 
#                 mozallowfullscreen 
#                 allowfullscreen 
#                 style="width: 944px; height: 530.528px;">
#         </iframe>
#     '''

# def main():
#     st.markdown(vimeo_video('303126374'), unsafe_allow_html=True)

# if __name__ == "__main__":
#     main()


# def link(link, text, **style):
#     return a(_href=link, _target="_blank", style=styles(**style))(text)


# def layout(*args):

#     style = """
#     <style>
#       # MainMenu {visibility: hidden;}
#       footer {visibility: hidden;}
#      .stApp { bottom: 105px; }
#     </style>
#     """

#     style_div = styles(
#         position="fixed",
#         left=0,
#         bottom=0,
#         margin=px(0, 0, 0, 0),
#         width=percent(100),
#         color="black",
#         text_align="center",
#         height="auto",
#         opacity=1
#     )

#     style_hr = styles(
#         display="block",
#         margin=px(8, 8, "auto", "auto"),
#         border_style="inset",
#         border_width=px(2)
#     )

#     body = p()
#     foot = div(
#         style=style_div
#     )(
#         hr(
#             style=style_hr
#         ),
#         body
#     )

#     st.markdown(style, unsafe_allow_html=True)

#     for arg in args:
#         if isinstance(arg, str):
#             body(arg)

#         elif isinstance(arg, HtmlElement):
#             body(arg)

#     st.markdown(str(foot), unsafe_allow_html=True)


# def footer():
#     myargs = [
#         "Made in ",
#         image('https://avatars3.githubusercontent.com/u/45109972?s=400&v=4',
#               width=px(25), height=px(25)),
#         " with ❤️ by ",
#         link("https://twitter.com/ChristianKlose3", "@ChristianKlose3"),
#         br(),
#         link("https://buymeacoffee.com/chrischross", image('https://i.imgur.com/thJhzOO.png')),
#     ]
#     layout(*myargs)


# if __name__ == "__main__":
#     footer()