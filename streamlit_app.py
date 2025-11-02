import streamlit as st
import requests

st.set_page_config(page_title="Drug Recommender App")

st.title(" Drug Recommender App")

# Input fields
age = st.number_input("Enter your Age", min_value=0, step=1)
gender = st.selectbox("Gender", ["male", "female"])
cholesterol = st.selectbox("Cholesterol Level", ["cholesterolHigh", "cholesterolLow"])
bp = st.selectbox("BP Level", ["bpHigh", "bpLow", "bpNormal"])
na_to_k = st.number_input("Enter Na_to_K Value", min_value=0.0, step=0.001, format="%.3f")

if st.button("Predict"):
    payload = {
        "age": age,
        "gender": gender,
        "cholesterol": cholesterol,
        "bp": bp,
        "na_to_k": na_to_k
    }
    
    try:
        response = requests.post("http://127.0.0.1:5000/predict", json=payload)
        result = response.json()
        st.success(f"Predicted Drug: {result['prediction']}")
    except Exception as e:
        st.error(f"Error connecting to backend: {e}")
