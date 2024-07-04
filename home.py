# home.py
import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from PyPDF2 import PdfReader
from nltk.corpus import stopwords
import string

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = ' '.join([word for word in text.split() if word not in stopwords.words("english")])
    return text

def home_page():
    st.title("Plagiarism Detection")
    
    
    uploaded_file1 = st.file_uploader("Upload PDF file 1", type="pdf")
    uploaded_file2 = st.file_uploader("Upload PDF file 2", type="pdf")

    if uploaded_file1 is not None and uploaded_file2 is not None:
        col1, col2 = st.columns(2)
        with col1:
            st.write("You have uploaded the following PDF file 1:")
            st.write(uploaded_file1.name)

        with col2:
            st.write("You have uploaded the following PDF file 2:")
            st.write(uploaded_file2.name)

        if st.button("Submit"):
            st.write("Submitted!")

            try:
                with st.spinner('Extracting text from PDF files...'):
                    pdf_reader1 = PdfReader(uploaded_file1)
                    text1 = ''.join(page.extract_text() for page in pdf_reader1.pages)
                    
                    pdf_reader2 = PdfReader(uploaded_file2)
                    text2 = ''.join(page.extract_text() for page in pdf_reader2.pages)

                text1 = preprocess_text(text1)
                text2 = preprocess_text(text2)

                cv = CountVectorizer()
                vectors = cv.fit_transform([text1, text2])

                cs = cosine_similarity(vectors)
                ans = cs[0, 1]
                ans1 = round(ans * 100, 2)

                msg = f"Similarity is: {ans1}%"
                background_color = "red" if ans1 > 60 else "green"
                styled_msg = f"<div style='text-align: center; background-color: {background_color}; padding: 10px;'>{msg}</div>"
                st.write(styled_msg, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Error: {e}")


            
