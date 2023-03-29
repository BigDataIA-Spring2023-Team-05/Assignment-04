import streamlit as st
import pandas as pd
import os

 
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# Heading of the webpage
st.write("# Welcome to MeetIn! 👋")
st.subheader(' This is a a Meeting Intelligence Application. We will be helping you with your audio transcribing and generate some questions based on the selected audio data.')

st.write('\n')
st.write('\n')

# link to the audio files and read the audio files
dirname = os.getcwd()

meet_file_1= dirname + "/data/audio_1.mp3"
meet_file_2= dirname + "/data/audio_2.mp3"
meet_file_3= dirname + "/data/audio_3.mp3"
meet_file_4= dirname + "/data/audio_meet_v.mp3"

# show the meeting recordings 
selected_audio_option = st.selectbox(
    'Please select the meeting from below options?',
    (meet_file_1, meet_file_2, meet_file_3, meet_file_4))

st.write('You selected:', selected_audio_option)


st.write("\n")

st.write("To listen to this audio click on play button. ")

st.audio(selected_audio_option, format='audio/mp3')

st.sidebar.success("Go to Transcribe page to see the transcribe of selected audio.")

# initialize
if 'audio_selected' not in st.session_state:
    st.session_state.audio_selected = 'none'

# set sidebar collapsed before clicking on Start with Transcribe button
if 'sidebar_state' not in st.session_state:
    st.session_state.sidebar_state = 'collapsed'

button_start = st.button('Start with Transcribe', key='but_start')

# hide collapsed control button
hide_bar = """
           <style>
           [data-testid='collapsedControl"] {visibility:hidden;}
           </style>
           """

# set sidebar expanded after login
if button_start:
    st.session_state.sidebar_state = 'expanded'
    st.session_state.audio_selected = selected_audio_option
else:
    st.session_state.sidebar_state = 'collapsed'
    st.markdown(hide_bar, unsafe_allow_html=True)
