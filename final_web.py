import os
import pickle

import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks', layout='wide', page_icon='🩺')

# Load models
diabetes_model = pickle.load (open("Models/final_diabetes_model.sav", 'rb'))
heartdisease_model = pickle.load (open("Models/final_heart_model.sav", 'rb'))
parkinsonsdisease_model = pickle.load (open("Models/final_parkinsons_model.sav", 'rb'))

# Centered Page Title
st.markdown("""<h1 style= 'text-align: center;'>Prediction of Disease Outbreak System (using ML) </h1>""", unsafe_allow_html=True)

# Horizontal Navigation Bar
selected = st.radio("", ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson’s Disease Prediction"], horizontal=True)

# Function to create the 3/4 - 1/4 Layout
def layout_section(input_fields, description_dict):
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader("Enter Patient Details")
        for field in input_fields:
            input_fields[field] = st.text_input(field, key=field)
    
    with col2:
        st.subheader("Feature Information")
        for key, value in description_dict.items():
            st.markdown(f"**{key}**: {value}")
    
    return input_fields

# Diabetes Prediction Section
if selected == "Diabetes Prediction":
    fields = {"Pregnancies": "", "Glucose Level": "", "Blood Pressure": "", "Skin Thickness": "", "Insulin Level": "", "BMI": "", "Diabetes Pedigree Function": "", "Age": ""}
    descriptions = {"Glucose": "Normal: 70-99 mg/dL", "Blood Pressure": "Normal: 120/80 mmHg", "BMI (Body Mass Index)": "Normal: 18.5-24.9"}
    user_input = layout_section(fields, descriptions)
    
    if st.button("Predict Diabetes"):
        if any(value.strip() == "" for value in user_input.values()):
            st.error("Error: All input fields must be filled!")
        else:
            user_values = [float(value) for value in user_input.values()]
            prediction = diabetes_model.predict([user_values])
            if prediction[0] == 1:
                st.success("The person is diabetic"  )
            else: 
                st.success("The person is not diabetic")

# Heart Disease Prediction Section
elif selected == "Heart Disease Prediction":
    fields = {
        "Age": "",
        "Sex (Enter 0 for Female, 1 for Male)": "",
        "CP (Chest Pain Type)": "",
        "Trestbps (Resting Blood Pressure)": "",
        "Chol (Cholesterol Level)": "",
        "FBS (Fasting Blood Sugar)": "",
        "RestECG (Resting ECG)": "",
        "Thalach (Max Heart Rate)": "",
        "Exang (Exercise Induced Angina)": "",
        "Oldpeak (ST Depression)": "",
        "Slope (Slope of Peak Exercise ST Segment)": "",
        "CA (Number of Major Vessels)": "",
        "Thal (Thalassemia Type)": ""
    }

    descriptions = {
        "Sex": "Enter 0 for Female, 1 for Male",
        "Chol": "Normal: <200 mg/dL",
        "FBS": "Normal: <100 mg/dL",
        "Trestbps": "Normal: 120/80 mmHg",
        "Oldpeak": "ST depression induced by exercise"
    }

    user_input = layout_section(fields, descriptions)

    if st.button("Predict Heart Disease"):
        if any(value.strip() == "" for value in user_input.values()):
            st.error("Error: All input fields must be filled!")
        else:
            user_values = [float(value) for value in user_input.values()]
            prediction = heartdisease_model.predict([user_values])
            if prediction[0] == 1:
                st.success("The person has heart disease")  
            else: 
                st.success("The person does not have heart disease")

# Parkinson’s Disease Prediction Section
elif selected == "Parkinson’s Disease Prediction":
    fields = {
        "MDVP:Fo(Hz)": "",
        "MDVP:Fhi(Hz)": "",
        "MDVP:Flo(Hz)": "",
        "MDVP:Jitter(%)": "",
        "MDVP:Jitter(Abs)": "",
        "MDVP:RAP": "",
        "MDVP:PPQ": "",
        "Jitter:DDP": "",
        "MDVP:Shimmer": "",
        "MDVP:Shimmer(dB)": "",
        "Shimmer:APQ3": "",
        "Shimmer:APQ5": "",
        "MDVP:APQ": "",
        "Shimmer:DDA": "",
        "NHR": "",
        "HNR": "",
        "RPDE": "",
        "DFA": "",
        "Spread1": "",
        "Spread2": "",
        "D2": "",
        "PPE": ""
    }

    descriptions = {
        "MDVP:Fo(Hz)": "Fundamental Frequency of Voice",
        "MDVP:Fhi(Hz)": "Highest Fundamental Frequency",
        "MDVP:Flo(Hz)": "Lowest Fundamental Frequency",
        "MDVP:Jitter(%)": "Variability in pitch (Jitter)",
        "MDVP:Jitter(Abs)": "Absolute Jitter",
        "MDVP:RAP": "Relative Amplitude Perturbation",
        "MDVP:PPQ": "Pitch Period Perturbation Quotient",
        "Jitter:DDP": "Average absolute difference of differences between consecutive pitch periods",
        "MDVP:Shimmer": "Variation in amplitude",
        "MDVP:Shimmer(dB)": "Shimmer in decibels",
        "Shimmer:APQ3": "Three-point Amplitude Perturbation Quotient",
        "Shimmer:APQ5": "Five-point Amplitude Perturbation Quotient",
        "MDVP:APQ": "Amplitude Perturbation Quotient",
        "Shimmer:DDA": "Average absolute differences of differences between consecutive periods in amplitude",
        "NHR": "Noise-to-Harmonics Ratio (higher values indicate voice disorders)",
        "HNR": "Harmonics-to-Noise Ratio (lower values indicate voice disorders)",
        "RPDE": "Recurrence Period Density Entropy (measures complexity of voice)",
        "DFA": "Detrended Fluctuation Analysis (measures signal randomness)",
        "Spread1": "Nonlinear measure of fundamental frequency variation",
        "Spread2": "Another measure of frequency variation",
        "D2": "Signal Complexity Measure",
        "PPE": "Pitch Period Entropy"
    }

    user_input = layout_section(fields, descriptions)

    if st.button("Predict Parkinson’s Disease"):
        if any(value.strip() == "" for value in user_input.values()):
            st.error("Error: All input fields must be filled!")
        else:
            user_values = [float(value) for value in user_input.values()]
            prediction = parkinsonsdisease_model.predict([user_values])
            if prediction[0] == 1:
                st.success("The person has Parkinson’s Disease")  
            else: 
                st.success("The person does not have Parkinson’s Disease")