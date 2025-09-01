import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
import os

# =======================
# Paths
# =======================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "best_model.pkl")
MANIFEST_PATH = os.path.join(BASE_DIR, "models", "feature_manifest.json")

# =======================
# Load model + manifest
# =======================
@st.cache_resource
def load_artifacts():
    model = joblib.load(MODEL_PATH)
    with open(MANIFEST_PATH, "r") as f:
        manifest = json.load(f)
    return model, manifest

model, manifest = load_artifacts()
expected_features = manifest["features"]

st.title("👨‍💼 Employee Attrition Prediction")
st.write("Fill in employee details and predict attrition risk.")

# =======================
# Build Input Form
# =======================

with st.form("employee_form"):
    st.subheader("📋 Employee Information")

    # Continuous numeric fields
    age = st.slider("Age", 18, 60, 30)
    distance = st.slider("Distance From Home (km)", 1, 30, 5)
    income = st.number_input("Monthly Income", min_value=1000, max_value=20000, value=5000, step=500)
    total_years = st.slider("Total Working Years", 0, 40, 5)
    years_company = st.slider("Years At Company", 0, 40, 3)
    job_sat = st.slider("Job Satisfaction (1–4)", 1, 4, 3)
    env_sat = st.slider("Environment Satisfaction (1–4)", 1, 4, 3)
    worklife = st.slider("Work Life Balance (1–4)", 1, 4, 3)

    # Encoded categorical fields
    gender = st.selectbox("Gender", ["Male", "Female"])
    overtime = st.selectbox("OverTime", ["Yes", "No"])
    marital = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])

    submitted = st.form_submit_button("🔍 Predict Attrition")

# =======================
# Map Inputs to Features
# =======================
if submitted:
    try:
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

        # Create dataframe
        input_df = pd.DataFrame([input_dict])

        # Ensure all expected features are present in the same order
        for col in expected_features:
            if col not in input_df.columns:
                input_df[col] = 0
        input_df = input_df[expected_features]

        # Predict
        proba = model.predict_proba(input_df)[0][1]
        pred = model.predict(input_df)[0]

        # =======================
        # Show Results
        # =======================
        st.success("✅ Prediction complete!")
        st.metric("Attrition Risk Probability", f"{proba:.2%}")
        if pred == 1:
            st.error("⚠️ High Attrition Risk: Employee likely to leave.")
        else:
            st.info("💼 Low Attrition Risk: Employee likely to stay.")

    except Exception as e:
        st.error(f"⚠️ Error during prediction: {e}")
