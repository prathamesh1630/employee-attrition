🏢 Employee Attrition Prediction System

🚀 A machine learning project to predict whether an employee is likely to leave the company, using the IBM HR Analytics Employee Attrition dataset.
Built with Python, scikit-learn, and Streamlit.

📂 Project Structure
├── app/                      # Streamlit app for prediction UI
├── data/                     # Raw & processed datasets
├── models/                   # Saved models & feature manifest
├── notebooks/                # Jupyter notebooks for EDA, training & tuning
│   └── src/                  # Helper scripts (feature list, utils, etc.)
├── .gitignore                # Ignore unnecessary files in Git
├── requirements.txt          # Project dependencies
└── README.md                 # Project description

📊 Dataset

Source: IBM HR Analytics Employee Attrition dataset

Rows: 1470

Features: 35 (26 numeric, 9 categorical)

Target: Attrition (Yes/No → encoded as 1/0)

⚙️ Installation

Clone the repository and install dependencies:

git clone https://github.com/your-repo/employee-attrition.git
cd employee-attrition
pip install -r requirements.txt

🚀 Usage
1. Data Exploration & Training

Run the notebooks inside the notebooks/ folder:

01_data_snapshot.ipynb → Load & preview dataset

02_eda.ipynb → Exploratory Data Analysis

03_feature_engineering.ipynb → Cleaning & encoding

04_model_training_baseline_models.ipynb → Train baseline models

05_model_tuning_and_insights.ipynb → Hyperparameter tuning + explainability

2. Streamlit App (Deployment UI)

Run the app locally:

streamlit run app/Streamlit_UI_app.py

📈 Model Performance
Model	Accuracy	Recall (Yes)	ROC-AUC
Logistic Regression	0.86	0.34	0.81
Random Forest	0.84	0.09	0.78

✅ Final Selected Model: Logistic Regression (tuned)

🔍 Key Insights

Younger employees & short tenure → higher attrition risk

Overtime → strongest predictor of attrition (30% vs 10%)

JobRole: Sales Representatives (~40% attrition) vs Research Directors (~2.5%)

Marital Status: Singles more likely to leave

Work-life balance & Job Satisfaction reduce attrition

📦 Deliverables

✅ Processed Data → data/processed/cleaned.csv

✅ Models → models/attrition_model.joblib

✅ Feature Manifest → models/feature_manifest.json

✅ Streamlit App → Interactive UI for predictions

🎯 Business Value

This system enables HR teams to:

Predict employee turnover risk early.

Understand why employees might leave (explainability).

Design retention strategies targeting overtime, job role, and satisfaction.

📌 Next Steps

Add batch predictions from uploaded CSV files.

Deploy with FastAPI + Docker for production.

Try SMOTE / class weights for improved recall on minority class.