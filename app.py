import streamlit as st
import pandas as pd
import numpy as np
import joblib

le_dict = joblib.load("label_encoders.pkl")
scaler = joblib.load("scaler.pkl")
pca = joblib.load("pca_model.pkl")
kmeans = joblib.load("kmeans_model.pkl")
dbscan = joblib.load("dbscan_model.pkl")

st.title("Coffee Health Clustering Prediction ☕🩺")

st.subheader("Enter Your Data")

Coffee_Intake = st.number_input("Coffee Intake (cups/day)", min_value=0.0, max_value=20.0, value=2.0)
Caffeine_mg = st.number_input("Caffeine (mg/day)", min_value=0.0, max_value=1000.0, value=100.0)
Sleep_Hours = st.number_input("Sleep Hours/day", min_value=0.0, max_value=24.0, value=7.0)
BMI = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)
Heart_Rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=200, value=70)
Physical_Activity_Hours = st.number_input("Physical Activity Hours/day", min_value=0.0, max_value=24.0, value=1.0)

Sleep_Quality = st.selectbox("Sleep Quality", le_dict['Sleep_Quality'].classes_)
Stress_Level = st.selectbox("Stress Level", le_dict['Stress_Level'].classes_)
Smoking = st.selectbox("Smoking", le_dict['Smoking'].classes_)
Alcohol_Consumption = st.selectbox("Alcohol Consumption", le_dict['Alcohol_Consumption'].classes_)

input_df = pd.DataFrame({
    'Coffee_Intake': [Coffee_Intake],
    'Caffeine_mg': [Caffeine_mg],
    'Sleep_Hours': [Sleep_Hours],
    'BMI': [BMI],
    'Heart_Rate': [Heart_Rate],
    'Physical_Activity_Hours': [Physical_Activity_Hours],
    'Sleep_Quality': [Sleep_Quality],
    'Stress_Level': [Stress_Level],
    'Smoking': [Smoking],
    'Alcohol_Consumption': [Alcohol_Consumption]
})

for col, le in le_dict.items():
    input_df[col] = le.transform(input_df[col])

features = ['Coffee_Intake', 'Caffeine_mg', 'Sleep_Hours', 'BMI', 'Heart_Rate', 'Physical_Activity_Hours',
            'Sleep_Quality', 'Stress_Level', 'Smoking', 'Alcohol_Consumption']
X_scaled = scaler.transform(input_df[features])

X_pca = pca.transform(X_scaled)

cluster_descriptions_km = {
    0: "Lower coffee intake, moderate health metrics",
    1: "Higher coffee intake with varying lifestyle and health features"
}

cluster_descriptions_db = {
    0: "Moderate coffee intake, healthy lifestyle metrics",
    1: "Higher coffee intake, slightly higher BMI & heart rate",
    2: "Low coffee intake, low physical activity",
    3: "High coffee intake, active lifestyle",
   -1: "Outliers / Noise points"
}

cluster_model = st.selectbox("Choose Model", ["KMeans", "DBSCAN"])

if st.button("Predict Cluster"):
    if cluster_model == "KMeans":
        kmeans_label = kmeans.predict(X_pca)[0]
        description = cluster_descriptions_km.get(kmeans_label, "No description available")
        st.success(f"KMeans Cluster: {kmeans_label} — {description}")
    else:
        dbscan_label = dbscan.fit_predict(X_pca)[0]
        description = cluster_descriptions_db.get(dbscan_label, "No description available")
        st.success(f"DBSCAN Cluster: {dbscan_label} — {description}")
