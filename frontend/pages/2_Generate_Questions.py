import streamlit as st
import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get('OPENAI_AP_KEY')

if st.session_state.sidebar_state == 'expanded':

    st.write("You have selected audio: ", st.session_state.audio_selected)
    st.write("Click on Generate Questions button below to get transcription of your audio.")   

    if st.session_state.transcribe_text == 'done':


        if 'generated_questions' not in st.session_state:
            st.session_state.generated_questions = ''

        st.write("Generate Questions")

        button_b = st.button('generate_questions_with_chatgpt', key='but_b')

        def generate_questions_with_chatgpt():
            # callable function
            # Load your API key from an environment variable or secret management service
            text = 'content ="'+ st.session_state.transcribed_text +'."'+ "Ask 4 questions about this given content."
            print(text)
            response = openai.Completion.create(
                model="text-davinci-003", prompt=text , temperature=0.5, max_tokens=500
            )
            # "Q: What was the meeting about?/n Q:How many participants are there in meeting?"
            return response['choices'][0]['text']

        # generate questions 
        if button_b:
            st.session_state.generated_questions = generate_questions_with_chatgpt()
            st.write('3-4 Questions on the above transcribed text: ')
            st.write(st.session_state.generated_questions)
            print(st.session_state.generated_questions)