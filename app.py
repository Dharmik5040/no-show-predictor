import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("noshow_model.pkl")

st.title("Clinic No-Show Predictor")
st.write("Enter patient details below to predict if they will show up for their appointment.")

# User inputs
gender = st.selectbox("Gender", ["Female", "Male"])
age = st.slider("Age", 0, 100, 30)
scholarship = st.selectbox("Scholarship", ["No", "Yes"])
hypertension = st.selectbox("Hypertension", ["No", "Yes"])
diabetes = st.selectbox("Diabetes", ["No", "Yes"])
alcoholism = st.selectbox("Alcoholism", ["No", "Yes"])
handcap = st.selectbox("Handicap", ["No", "Yes"])
sms_received = st.selectbox("SMS Received", ["No", "Yes"])

# Convert to numeric
data = pd.DataFrame([[
    0 if gender == "Female" else 1,
    age,
    1 if scholarship == "Yes" else 0,
    1 if hypertension == "Yes" else 0,
    1 if diabetes == "Yes" else 0,
    1 if alcoholism == "Yes" else 0,
    1 if handcap == "Yes" else 0,
    1 if sms_received == "Yes" else 0
]], columns=['Gender', 'Age', 'Scholarship', 'Hipertension', 'Diabetes', 'Alcoholism', 'Handcap', 'SMS_received'])

# Prediction
if st.button("Predict"):
    prediction = model.predict(data)[0]
    result = "❌ No-Show" if prediction == 1 else "✅ Will Show"
    st.subheader(f"Prediction: {result}")
