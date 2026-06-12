import streamlit as st
from rag_core import ask_pdf

# 1. Instruct the browser engine to configure header title tags
st.set_page_config(page_title="AI Document App", layout="centered")
st.title("Intelligent PDF Research Assistant")
st.write("The local document index engine is operational. Submit questions to extract verified source responses.")

# 2. Render an interactive text input prompt block box on screen
user_input = st.text_input("Type your query regarding the document context here:")

# 3. Execute logical pipeline if data is present inside the input block
if user_input:
    with st.spinner("Scanning local database vector blocks for verifying facts..."):
        # Trigger the functional backend Day 6 query logic pipeline
        answer = ask_pdf(user_input)
        
        # Output the verified generated answer onto the screen layout elements
        st.subheader("Verified AI Response:")
        st.info(answer)

