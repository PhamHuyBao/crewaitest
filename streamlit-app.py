from io import StringIO
import streamlit as st
import pandas as pd
import main as agent
st.set_page_config(page_title="email wrapping")

uploaded_file = st.file_uploader(label="upload your email csv")
email_template = st.text_area(label="Email Template")

isClick = st.button("Generated Email", type="primary")

if isClick: 
    if uploaded_file and email_template is not None:
        bytes_data = uploaded_file.getvalue()
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        result = agent.generate_email(email_template, stringio)
        st.markdown(result)
        st.download_button('Download Generated Email', result, file_name="generated_email")




