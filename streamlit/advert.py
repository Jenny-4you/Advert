import joblib
import numpy as np
import streamlit as st
import os

try:
    model_path = 'Sales_model.pkl'
    if  os.path.exists(model_path):
        model = joblib.load(model_path)
        st.success('Model loaded Successfully')
    else:
        st.error("Model file not found")
except Exception as e:
    zst.error(f"Error loading model: {str(e)}")
# unswr input
tv_budget = st.slider('TV Ad Budget', 0, 300, 100)
radio_budget = st.slider('Radio Ad Budget', 0, 100, 20)
newspaper_budget = st.slider('Newspaper Ad Budget', 0, 200, 20)

# prediction
if  'model' in locals():
    input_data = np.array([[ tv_budget, radio_budget, newspaper_budget ]])
    predicted_sales = model.predict(input_data)[0]
    st.write(f"Predicted Sales: {predicted_sales:.2f}")






    