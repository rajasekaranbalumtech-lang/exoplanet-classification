import streamlit as st
import pandas as pd
import joblib

# Load saved models
models = {
    "Logistic Regression": joblib.load("model/logistic_regression.pkl"),
    "Decision Tree": joblib.load("model/decision_tree.pkl"),
    "KNN": joblib.load("model/knn.pkl"),
    "Naive Bayes": joblib.load("model/naive_bayes.pkl"),
    "Random Forest": joblib.load("model/random_forest.pkl"),
    "XGBoost": joblib.load("model/xgboost.pkl"),
}

st.title("Exoplanet Classification App")

# Model selection
model_choice = st.selectbox(
    "Choose a model:",
    list(models.keys())
)

# File upload
uploaded_file = st.file_uploader("Upload CSV file for prediction", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Uploaded Data Preview:", data.head())

    # Run prediction
    model = models[model_choice]
    preds = model.predict(data)

    st.subheader("Predictions")
    st.write(preds)
