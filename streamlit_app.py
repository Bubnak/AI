import streamlit as st
import requests

st.title("Text Summarization App")

input_text = st.text_area("Enter text to summarize")

if st.button("Summarize"):
    if input_text:
        # Replace 'localhost' with the appropriate Docker container name or host IP
        api_url = 'http://localhost:5000/summarize'  # Adjust this URL to match your Flask API
        response = requests.post(api_url, json={"text": input_text})

        if response.status_code == 200:
            summary = response.json().get('summary', '')
            st.write("Summary:", summary)
        else:
            st.write("Error:", response.status_code)
    else:
        st.write("Please enter text to summarize.")