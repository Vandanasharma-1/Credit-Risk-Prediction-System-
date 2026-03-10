import streamlit as st
import pandas as pd
import pickle

# Load the saved model
model = pickle.load(open('credit_model.pkl', 'rb'))

st.title("Credit Risk Prediction System")
st.markdown("Enter the applicant's details below to assess loan risk.")

# User Inputs
col1, col2 = st.columns(2)
with col1:
    income = st.number_input("Annual Income ($)", min_value=0)
    loan_amount = st.number_input("Loan Amount ($)", min_value=0)
with col2:
    emp_length = st.slider("Employment Length (Years)", 0, 40, 5)
    region = st.selectbox("Region", ["West", "MidWest", "SouthEast", "SouthWest", "NorthEast"])

# Prediction Logic
if st.button("Predict Risk"):
    # Preprocess inputs to match your model's training format
    # Example: input_data = [income, loan_amount, emp_length, region_encoded]
    prediction = model.predict(['features'])[0]
    
    if prediction == 1:
        st.error("High Risk: Potential Default Predicted")
    else:
        st.success("Low Risk: Safe to Proceed")