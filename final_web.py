import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks', layout='wide', page_icon='🩺')

# Load models
diabetes_model = pickle.load(open("Models/final_diabetes_model.sav", 'rb'))
heartdisease_model = pickle.load(open("Models/final_heart_model.sav", 'rb'))
parkinsonsdisease_model = pickle.load(open("Models/final_parkinsons_model.sav", 'rb'))

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
            st.success("The person is diabetic" if prediction[0] == 1 else "The person is not diabetic")

# Heart Disease Prediction Section
elif selected == "Heart Disease Prediction":
    fields = {"Age": "", "Sex": "", "CP (Chest Pain Type)": "", "Trestbps (Resting Blood Pressure)": "", "Cholesterol": "", "FBS (Fasting Blood Sugar)": "", "RestECG (Resting ECG)": "", "Thalach (Max Heart Rate)": "", "Exang (Exercise Induced Angina)": "", "Oldpeak": "", "CA (Number of major vessels colored by fluoroscopy)": "", "Thal (Thalassemia type)": ""}
    descriptions = {"Cholesterol": "Normal: <200 mg/dL", "FBS": "Normal: <100 mg/dL", "Trestbps": "Normal: 120/80 mmHg"}
    user_input = layout_section(fields, descriptions)
    
    if st.button("Predict Heart Disease"):
        if any(value.strip() == "" for value in user_input.values()):
            st.error("Error: All input fields must be filled!")
        else:
            user_values = [float(value) for value in user_input.values()]
            prediction = heartdisease_model.predict([user_values])
            st.success("The person has heart disease" if prediction[0] == 1 else "The person does not have heart disease")

# Parkinson’s Disease Prediction Section
elif selected == "Parkinson’s Disease Prediction":
    fields = {"MDVP:Fo(Hz)": "", "MDVP:Jitter(%)": "", "MDVP:Shimmer": "", "NHR": "", "HNR": "", "RPDE": "", "DFA": "", "Spread1": "", "PPE": ""}
    descriptions = {"MDVP:Fo(Hz)": "Fundamental Frequency of Voice", "MDVP:Jitter(%)":"Variability in pitch (Jitter)","MDVP:Shimmer":"Variation in amplitude","NHR":"Noise-to-Harmonics Ratio (higher values indicate voice disorders)", "HNR": "Harmonics-to-Noise Ratio (lower values indicate voice disorders)", "RPDE":"Recurrence Period Density Entropy (measures complexity of voice)", "DFA":"Detrended Fluctuation Analysis (measures signal randomness)", "Spread1":"Nonlinear measure of fundamental frequency variation", "PPE": "Pitch Period Entropy"}
    user_input = layout_section(fields, descriptions)
    
    if st.button("Predict Parkinson’s Disease"):
        if any(value.strip() == "" for value in user_input.values()):
            st.error("Error: All input fields must be filled!")
        else:
            user_values = [float(value) for value in user_input.values()]
            prediction = parkinsonsdisease_model.predict([user_values])
            st.success("The person has Parkinson’s Disease" if prediction[0] == 1 else "The person does not have Parkinson’s Disease")
