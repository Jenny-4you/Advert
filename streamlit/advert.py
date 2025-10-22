import joblib
import numpy as np
import streamlit as st
import os

st.title("Sales Prediction App")

try:
    # Use absolute path for reliability
    model_path = os.path.join(os.path.dirname(__file__), 'Sales_model.pkl')

    if os.path.exists(model_path):
        model = joblib.load(model_path)
        st.success('✅ Model loaded successfully')
    else:
        st.error("❌ Model file not found. Make sure 'Sales_model.pkl' is in the same directory.")
except Exception as e:
    st.error(f"⚠️ Error loading model: {str(e)}")

# User input
tv_budget = st.slider('TV Ad Budget', 0, 300, 100)
radio_budget = st.slider('Radio Ad Budget', 0, 100, 20)
newspaper_budget = st.slider('Newspaper Ad Budget', 0, 200, 20)

# Prediction
if 'model' in locals():
    input_data = np.array([[tv_budget, radio_budget, newspaper_budget]])
    predicted_sales = model.predict(input_data)[0]
    st.write(f"📈 Predicted Sales: **{predicted_sales:.2f}**")
