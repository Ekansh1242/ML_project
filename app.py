import streamlit as st
import joblib
import numpy as np

# App Config
st.set_page_config(page_title="Drug Recommender App", page_icon="💊", layout="centered")

# Title
st.title("💊 Drug Recommender App")

# Load trained model
@st.cache_resource
def load_model():
    return joblib.load("drug-recommender.pkl")

model = load_model()

# Input fields
age = st.number_input("Enter your Age", min_value=0, step=1)
gender = st.selectbox("Gender", ["male", "female"])
cholesterol = st.selectbox("Cholesterol Level", ["cholesterolHigh", "cholesterolLow", "cholestrolNormal"])
bp = st.selectbox("BP Level", ["bpHigh", "bpLow", "bpNormal"])
na_to_k = st.number_input("Enter Na_to_K Value", min_value=0.0, step=0.001, format="%.3f")

# Predict button
if st.button("Predict Drug"):
    # Preprocess inputs
    Male = 1 if gender == 'male' else 0
    Cholesterol_Status = 1 if cholesterol == 'cholesterolHigh' else 0

    if bp == 'bpHigh':
        BP_HIGH = 1
        BP_LOW = 0
    elif bp == 'bpLow':
        BP_HIGH = 0
        BP_LOW = 1
    else:
        BP_HIGH = 0
        BP_LOW = 0

    # Prepare input for model
    input_data = np.array([[age, Male, Cholesterol_Status, na_to_k, BP_HIGH, BP_LOW]])

    # Make prediction
    prediction = model.predict(input_data)

    st.success(f"💊 Recommended Drug: **{prediction[0]}**")
