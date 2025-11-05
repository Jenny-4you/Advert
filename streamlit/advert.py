import joblib
import numpy as np
import streamlit as st
import os

st.title("Sales Prediction App")

# Use relative path
model_path = "Sales_model.pkl"

# Debug info (optional)
st.write("📁 Current working directory:", os.getcwd())
st.write("📂 Files in directory:", os.listdir())

# Try loading model
if os.path.exists(model_path):
    model = joblib.load(model_path)
    st.success("✅ Model loaded successfully!")
else:
    st.error("❌ Model file not found. Make sure 'Sales_model.pkl' is in the same GitHub repo as app.py.")
    st.stop()

# Input sliders
tv_budget = st.slider('TV Ad Budget', 0, 300, 100)
radio_budget = st.slider('Radio Ad Budget', 0, 100, 20)
newspaper_budget = st.slider('Newspaper Ad Budget', 0, 200, 20)

# Prediction
input_data = np.array([[tv_budget, radio_budget, newspaper_budget]])
predicted_sales = model.predict(input_data)[0]
st.write(f"📈 Predicted Sales: **{predicted_sales:.2f}**")
