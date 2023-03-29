import streamlit as st
import whisper


if st.session_state.sidebar_state == 'expanded':

    # initialize
    st.session_state.transcribe_text = 'none'

    st.write("You have selected audio: ", st.session_state.audio_selected)
    st.write("Click on Transcribe button below to get transcription of your audio.")    

    if 'transcribed_text' not in st.session_state:
        st.session_state.transcribed_text = ''

    button_a = st.button('transcribe_with_whisper', key='but_a')

    def transcribe_with_whisper():
        # callable function
        model = whisper.load_model("base")
        result = model.transcribe(st.session_state.audio_selected)
        print("transcribed data with whisper")
        print("type(result['text']): ", type(result["text"]))
        print(result["text"])
        return result["text"]

    if button_a:
        st.session_state.transcribed_text = transcribe_with_whisper()
        st.write('Transcribed Text is given below:')
        st.write("\n")
        st.write(st.session_state.transcribed_text)
        st.session_state.disabled = False
        st.session_state.transcribe_text = 'done'
