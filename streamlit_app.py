import streamlit as st
import numpy as np
import os
from src.project.pipeline.prediction import PredictionPipeline

# Streamlit App
st.set_page_config(page_title="Wine Quality Prediction", layout="centered")

st.title("Wine Quality Prediction App")

# Sidebar menu
menu = ["Home", "Train Model", "Predict"]
choice = st.sidebar.radio("Navigate", menu)

if choice == "Home":
    st.subheader("Welcome to the Wine Quality Prediction App")
    st.write("""
    This app allows you to:
    - Train a new wine quality prediction model
    - Input wine characteristics and predict quality
    """)
    
elif choice == "Train Model":
    st.subheader("Train Model")
    if st.button("Start Training"):
        with st.spinner("Training in progress..."):
            os.system("python main.py")
        st.success("✅ Training Successful!")

elif choice == "Predict":
    st.subheader("Predict Wine Quality")

    with st.form(key="prediction_form"):
        fixed_acidity = st.number_input("Fixed Acidity", value=7.4)
        volatile_acidity = st.number_input("Volatile Acidity", value=0.7)
        citric_acid = st.number_input("Citric Acid", value=0.0)
        residual_sugar = st.number_input("Residual Sugar", value=1.9)
        chlorides = st.number_input("Chlorides", value=0.076)
        free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", value=11.0)
        total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", value=34.0)
        density = st.number_input("Density", value=0.9978)
        pH = st.number_input("pH", value=3.51)
        sulphates = st.number_input("Sulphates", value=0.56)
        alcohol = st.number_input("Alcohol", value=9.4)

        submit_button = st.form_submit_button(label="Predict")

    if submit_button:
        try:
            data = [
                fixed_acidity,
                volatile_acidity,
                citric_acid,
                residual_sugar,
                chlorides,
                free_sulfur_dioxide,
                total_sulfur_dioxide,
                density,
                pH,
                sulphates,
                alcohol
            ]
            data = np.array(data).reshape(1, 11)

            obj = PredictionPipeline()
            predict = obj.predict(data)

            st.success(f"Predicted Wine Quality: **{predict}**")
        except Exception as e:
            st.error(f"Something went wrong: {e}")
