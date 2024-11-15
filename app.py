# =======================       IMPORTS       ========================== #

import streamlit as st
import pandas as pd
import zipfile
import gdown
import os
import warnings  # Suppress warnings
import streamlit.components.v1 as components
from datetime import datetime
from scraper_deter import scraper

# scraper()



# Set environment variable to suppress Streamlit warnings
warnings.filterwarnings("ignore")  # Suppress all Python warnings
# OOh lalalalalal
# =======================    PAGE CONFIG    ========================== #
icon = "🌳"

st.set_page_config(
    page_title="DETER",
    page_icon=icon,
    layout="wide",
    initial_sidebar_state= "expanded"
)

# =======================    CSS for Custom Theme    ========================== #
st.markdown("""
    <style>
    /* Background color */
    .stApp {
        background-color: #D8DEE9;
    }

    /* Sidebar styling */
    .css-1d391kg {  
        background-color: #D8DEE9;
    }
    .css-1d391kg .stButton>button, .css-1d391kg h2 {
        color: #000000;  /* Dark text for contrast */
    }

    /* Text and title colors */
    .stMarkdown h1, h2, h3, h4, h5, h6, .stMarkdown p, .stTextInput, .stButton>button {
        color: #000000;  /* Dark text for general content */
        background-color: transparent;
    }

    /* Button styling */
    .stButton>button {
        color: #FFFFFF; /* White text on buttons */
        background-color: #81a1c1;
        border: none;
    }
    .stButton>button:hover {
        background-color: #5e81ac;
    }

    /* Divider and footer text color */
    hr, .footer h6 {
        color: #000000;
    }

    /* Header and sidebar link hover effect */
    .stMarkdown h3 {
        color: #000000;
    }

    /* Table styling (if any) */
    .dataframe, .stDataFrame {
        background-color: #88c0d0;
        color: #000000;
        border: 1px solid #5e81ac;
    }

    /* Sidebar navigation links */
    .sidebar-link {
        color: #000000;
        text-decoration: none;
        font-size: 18px;
        display: block;
        padding: 8px 16px;
    }
    .sidebar-link:hover {
        background-color: #81a1c1;
        color: #FFFFFF;
    }
    </style>
    """, unsafe_allow_html=True)

# =======================    Download Maps    ========================== #
def toast_msg():
    pass  # Removed language-related toast messages

def isMapsDownloaded():
    folder = 'Visualizations/DETER/Maps'
    os.makedirs(folder, exist_ok=True)
    total = 22

    downloaded = False
    
    if os.path.exists(folder):
        num = len([nome for nome in os.listdir(folder)])
        if num >= total:
            downloaded = True

    return downloaded



# =======================       TEXTS       ========================== #

df_texts = pd.read_csv('texts/texts_deter.csv', sep='§', engine='python')
english = {df_texts['Key'][i]: df_texts['English'][i] for i in range(len(df_texts))}

classes_deter_en = {
    'CICATRIZ_DE_QUEIMADA': 'Forest Fire Scar',
    'DESMATAMENTO_CR': 'Deforestation with Exposed Soil',
    'DESMATAMENTO_VEG': 'Deforestation with Vegetation',
    'MINERACAO': 'Mining',
    'DEGRADACAO': 'Degradation',
    'CS_DESORDENADO': 'Selective Logging Type 1 (Disordered)',
    'CS_GEOMETRICO': 'Selective Logging Type 2 (Geometric)',
}

estados = {
    "MT": "Mato Grosso",
    "PA": "Pará",
    "AM": "Amazonas",
    "RO": "Rondônia",
    "MA": "Maranhão",
    "RR": "Roraima",
    "AC": "Acre",
    "TO": "Tocantins",
    "AP": "Amapá"
}

def get_texts(lang):
    return classes_deter_en, english  # Default to English

# ======================= DEFAULT LANGUAGE SETTINGS ========================== #
current_lang = 'en'
selected_language = 'English'

dict_classes, texts = get_texts(selected_language)

# =======================      HEADER       ========================== #

def center_md(text):
    return "<h3 style='text-align: center;'>" + text + "</h3>"
        
st.markdown(center_md(texts['page_title']), unsafe_allow_html=True)
st.image('Images/deforestation.png') 

# =======================        BODY       ========================== #

def divider():
    st.markdown('</br>', unsafe_allow_html=True)
    st.divider()
    st.markdown('</br>', unsafe_allow_html=True)

# Sidebar Navigation with clickable text links
navigation_options = [
    texts['about'],
    texts['map'],
    texts['alert_classes'],
    texts['states_statistics'],
    texts['cities_statistics'],
    texts['ucs_statistics'],
    texts['dmg_ty']
]

# Use query parameters to track the selected page
nav_params = st.experimental_get_query_params()
if "page" in nav_params:
    selected_page = nav_params["page"][0]
else:
    selected_page = texts['about']

def nav_link(text, key):
    href = f'?page={key}'
    # Added target="_self" to ensure the link opens in the same tab
    st.sidebar.markdown(f'<a href="{href}" target="_self" class="sidebar-link">{text}</a>', unsafe_allow_html=True)

# Display navigation links
for option in navigation_options:
    nav_link(option, option)

# =======================        MAPS       ========================== #
def center_map(html_map):
    html_final = """
    <div style='display:flex; justify-content:center; align-items:center; height:100%;'>
    <div style='width: 80%;'>""" + html_map + """</div>
    </div>
    """
    return html_final

def read_map(map_name):
    html_file_path = f'Visualizations/DETER/Maps/{map_name}.html'
    
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    return html_content

# =======================        GRAPHS       ========================== #
def plot_graph(name, format='png', language=current_lang):
    dir = "Visualizations/DETER/Graphs"
    img_name = f"{name}_{language.upper()}.{format}"
    img_path = os.path.join(dir, img_name)
    
    if os.path.exists(img_path):
        st.image(img_path)
    else:
        st.error(f"Image {img_name} not found.")

def read_txt_graph(name):
    dir = "Visualizations/DETER/Graphs"
    file_name = name + '.txt'
    file_path = os.path.join(dir, file_name)
    
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as txt:
            return txt.read()
    else:
        print(f"File {file_name} not found.")
        

# Display content based on selected page
if selected_page == texts['about']:
    st.write(texts['deter_expander_desc_1'])
    st.write(texts['deter_expander_desc_2'])
    divider()

elif selected_page == texts['map']:
    radio_title = texts['vis_type']
    options = texts['vis_options'].split(';')

    seL_map = st.radio(radio_title, options=options,
                           horizontal=True, index=0)

    if seL_map == options[1]:
        map_name = 'States_' + current_lang.upper()
        with st.spinner(text="Loading..."):
            components.html(read_map(map_name), height=900)
            
    elif seL_map == options[2]:
        df_estados = pd.DataFrame(list(estados.items()), columns=['UF', 'Nome'])
        df_estados['Nome_UF'] = df_estados['Nome'] + ' (' + df_estados['UF'] + ')'
        
        lst_states = list(df_estados['Nome_UF'])
        
        ms_title = texts['vis_state']
        option = st.selectbox(
            ms_title,
            tuple(lst_states))

        uf_sel = df_estados[df_estados['Nome_UF'] == option].UF.values[0]

        map_name = 'Cities_' + current_lang.upper() + '_' + uf_sel.upper()
        
        with st.spinner('Loading visualization, please wait...'):
            components.html(read_map(map_name), height=900)
        
        
    elif seL_map == options[3]:
        map_name = 'C_Units_' + current_lang.upper()
        with st.spinner(text="Loading..."):
            components.html(read_map(map_name), height=900)
    divider()

elif selected_page == texts['alert_classes']:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(center_md(texts['title_deter_graph2']), unsafe_allow_html=True)
        plot_graph('Graph2')
        
    with col2:
        st.markdown(center_md(texts['title_deter_graph1']), unsafe_allow_html=True)
        plot_graph('Graph1')


    st.markdown(texts['graphs_12_desc'])
    divider()

elif selected_page == texts['states_statistics']:
    st.markdown(center_md(texts['title_deter_graph3']), unsafe_allow_html=True)
    plot_graph('Graph3')
    st.markdown(texts['graph3_desc'])
    
    divider()

    st.markdown(center_md(texts['graph8_title']), unsafe_allow_html=True)
    plot_graph('Graph8')
    st.markdown(texts['graph8_desc'])
    divider()

elif selected_page == texts['cities_statistics']:
    st.markdown(center_md(texts['title_deter_graph4']), unsafe_allow_html=True)
    plot_graph('Graph4')
    st.markdown(texts['graph4_desc'])
    divider()
    
elif selected_page == texts['ucs_statistics']:
    st.markdown(center_md(texts['graph9_title']), unsafe_allow_html=True)
    plot_graph('Graph9')
    st.markdown(texts['graph9_desc'])

    divider()

elif selected_page == texts['dmg_ty']:
    st.markdown(center_md(texts['title_deter_graph5']), unsafe_allow_html=True)
    plot_graph('Graph5')
    st.markdown(texts['graph5_desc'])
    
    divider()
    
    period = read_txt_graph('Graph6_' + current_lang.upper() + '_period')
    if period:
        period = period.split(';')
        st.markdown(center_md(texts['title_deter_graph6'].format(period[0], period[1])), unsafe_allow_html=True)
        plot_graph('Graph6')
        st.markdown(texts['graph6_desc'])
    else:
        st.error("Period data not found.")
    divider()

    st.markdown(center_md(texts['title_deter_graph7']), unsafe_allow_html=True)
    plot_graph('Graph7')
    st.markdown(texts['graph7_desc'], unsafe_allow_html=True)
    divider()

# =======================        FOOTER       ========================== #

from PIL import Image

# Load the image
image = Image.open("Images/gt.png")

# Display the image centered
st.markdown(
    "<div style='display: flex; justify-content: center;'>",
    unsafe_allow_html=True
)
st.image(image, caption="", use_column_width=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<h6 style='text-align: center;'>Aarushi Dhanuka, Arvind Ram, Prathiba Narayan, Sakthi Pasupathy, Sanjana Chillara, Shail Patel </h6>", unsafe_allow_html=True)