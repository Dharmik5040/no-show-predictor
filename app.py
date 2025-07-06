import streamlit as st
import pandas as pd
import joblib

# Load your trained model
model = joblib.load("noshow_model.pkl")

st.title("🩺 Clinic No-Show Predictor")

st.write("Enter patient details to predict whether they will show up for their appointment.")

# User input form
gender = st.selectbox("Gender", ["Female", "Male"])
age = st.slider("Age", 0, 100, 30)
scholarship = st.selectbox("On Scholarship?", ["No", "Yes"])
hypertension = st.selectbox("Has Hypertension?", ["No", "Yes"])
diabetes = st.selectbox("Has Diabetes?", ["No", "Yes"])
alcoholism = st.selectbox("Alcoholism History?", ["No", "Yes"])
handcap = st.selectbox("Is Handicapped?", ["No", "Yes"])
sms_received = st.selectbox("Received SMS Reminder?", ["No", "Yes"])

# Convert to input format
input_data = pd.DataFrame([[
    0 if gender == "Female" else 1,
    age,
    1 if scholarship == "Yes" else 0,
    1 if hypertension == "Yes" else 0,
    1 if diabetes == "Yes" else 0,
    1 if alcoholism == "Yes" else 0,
    1 if handcap == "Yes" else 0,
    1 if sms_received == "Yes" else 0
]], columns=['Gender', 'Age', 'Scholarship', 'Hipertension', 'Diabetes', 'Alcoholism', 'Handcap', 'SMS_received'])

# Predict and display
if st.button("Predict"):
    result = model.predict(input_data)[0]
    st.subheader("Prediction:")
    st.success("✅ Likely to Show" if result == 0 else "❌ Likely to No-Show")
