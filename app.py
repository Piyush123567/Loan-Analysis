import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("loan_approval_model.pkl")

st.title("🏦 Loan Approval Prediction App")
st.write("Enter applicant details to predict loan approval")

# User inputs
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
credit_history = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

applicant_income_log = st.number_input("Applicant Income (log)", value=8.5)
loan_amount_log = st.number_input("Loan Amount (log)", value=4.8)
loan_term_log = st.number_input("Loan Term (log)", value=5.8)
total_income_log = st.number_input("Total Income (log)", value=8.6)

# Create dataframe
input_df = pd.DataFrame({
    "Gender": [gender],
    "Married": [married],
    "Dependents": [dependents],
    "Education": [education],
    "Self_Employed": [self_employed],
    "Credit_History": [credit_history],
    "Property_Area": [property_area],
    "ApplicantIncomelog": [applicant_income_log],
    "LoanAmountlog": [loan_amount_log],
    "Loan_Amount_Term_log": [loan_term_log],
    "Total_Income_log": [total_income_log]
})

# Predict
if st.button("Predict Loan Approval"):
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")
