"""Streamlit interface for the employee attrition model."""

import json
import os

import joblib
import pandas as pd
import streamlit as st


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "best_model.pkl")
MANIFEST_PATH = os.path.join(BASE_DIR, "models", "feature_manifest.json")


@st.cache_resource
def load_artifacts():
    model = joblib.load(MODEL_PATH)
    with open(MANIFEST_PATH, encoding="utf-8") as manifest_file:
        manifest = json.load(manifest_file)
    return model, manifest


st.title("Employee Attrition Prediction")
st.write("Enter employee details to estimate attrition risk.")
st.caption(
    "For educational demonstration only. This estimate should not be used to make "
    "employment decisions."
)

if not os.path.exists(MODEL_PATH) or not os.path.exists(MANIFEST_PATH):
    st.error(
        "Model artifacts are missing. Run the data preparation and model training "
        "notebooks described in the README, then restart this app."
    )
    st.stop()

model, manifest = load_artifacts()
expected_features = manifest["features"]

with st.form("employee_form"):
    st.subheader("Employee Information")

    age = st.slider("Age", 18, 60, 30)
    distance = st.slider("Distance from home (km)", 1, 30, 5)
    income = st.number_input(
        "Monthly income", min_value=1000, max_value=20000, value=5000, step=500
    )
    total_years = st.slider("Total working years", 0, 40, 5)
    years_company = st.slider("Years at company", 0, 40, 3)
    job_sat = st.slider("Job satisfaction (1-4)", 1, 4, 3)
    env_sat = st.slider("Environment satisfaction (1-4)", 1, 4, 3)
    worklife = st.slider("Work-life balance (1-4)", 1, 4, 3)

    gender = st.selectbox("Gender", ["Male", "Female"])
    overtime = st.selectbox("Overtime", ["Yes", "No"])
    marital = st.selectbox("Marital status", ["Single", "Married", "Divorced"])
    submitted = st.form_submit_button("Predict attrition risk")

if submitted:
    input_dict = {
        "Age": age,
        "DistanceFromHome": distance,
        "MonthlyIncome": income,
        "TotalWorkingYears": total_years,
        "YearsAtCompany": years_company,
        "JobSatisfaction": job_sat,
        "EnvironmentSatisfaction": env_sat,
        "WorkLifeBalance": worklife,
        "Gender_encoded": 1 if gender == "Male" else 0,
        "OverTime_encoded": 1 if overtime == "Yes" else 0,
        "MaritalStatus_Divorced": 1 if marital == "Divorced" else 0,
        "MaritalStatus_Married": 1 if marital == "Married" else 0,
        "MaritalStatus_Single": 1 if marital == "Single" else 0,
    }
    input_df = pd.DataFrame([input_dict])
    for feature in expected_features:
        if feature not in input_df.columns:
            input_df[feature] = 0
    input_df = input_df[expected_features]

    probability = model.predict_proba(input_df)[0][1]
    prediction = model.predict(input_df)[0]

    st.metric("Estimated attrition probability", f"{probability:.1%}")
    if prediction == 1:
        st.warning("The model classifies this input as higher attrition risk.")
    else:
        st.info("The model classifies this input as lower attrition risk.")
