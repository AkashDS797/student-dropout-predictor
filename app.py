import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Student Retention Analytics", layout="centered")

model = joblib.load('dropout_model_lite.pkl')

st.title("Student Retention Analytics")
st.markdown("---")
st.markdown("Input student parameters below to execute real-time dropout risk analysis.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Financial & Demographic")
    tuition_up_to_date = st.radio("Tuition Fees Up To Date?", ["Yes", "No"])
    scholarship = st.radio("Active Scholarship?", ["Yes", "No"])
    age = st.slider("Age at Enrollment", 16, 50, 19)

with col2:
    st.subheader("Academic Performance")
    sem1_approved = st.slider("1st Sem Units Approved", 0, 15, 5)
    sem2_approved = st.slider("2nd Sem Units Approved", 0, 15, 5)
    sem2_grade = st.slider("2nd Sem Grade Average", 0.0, 20.0, 12.0)

tuition_val = 1 if tuition_up_to_date == "Yes" else 0
scholarship_val = 1 if scholarship == "Yes" else 0

input_data = pd.DataFrame([[
    tuition_val, scholarship_val, age, sem1_approved, sem2_approved, sem2_grade
]], columns=[
    'Tuition fees up to date', 'Scholarship holder', 'Age at enrollment',
    'Curricular units 1st sem (approved)', 'Curricular units 2nd sem (approved)',
    'Curricular units 2nd sem (grade)'
])

st.markdown("---")
if st.button("Execute Predictive Analysis", type="primary", use_container_width=True):
    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]
    
    st.subheader("System Output:")
    
    if prediction == 0:
        st.error(f"Status: High Risk of Dropout. (Confidence: {probabilities[0]*100:.1f}%)")
        st.markdown("> **Recommendation:** Flag for immediate academic counseling and financial aid review.")
    else:
        st.success(f"Status: On Track for Graduation. (Confidence: {probabilities[1]*100:.1f}%)")
        st.markdown("> **Recommendation:** Standard monitoring. No critical intervention required.")
