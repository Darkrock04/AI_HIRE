import streamlit as st
import requests

# The URL of our FastAPI backend
BACKEND_URL = "http://localhost:8000/predict"

st.set_page_config(page_title="Salary Predictor", page_icon="💰", layout="centered")

st.title("💸 Salary Predictor")

st.markdown("---")

# Slider for User Input
years_exp = st.slider("Select Years of Experience:", min_value=0.0, max_value=30.0, value=5.0, step=0.1)

st.write(f"**Candidate Experience:** {years_exp} Years")

if st.button("Predict Expected Salary", type="primary"):
    # Send the data to the FastAPI Backend
    payload = {"years_experience": years_exp}
    
    try:
        response = requests.post(BACKEND_URL, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            predicted_salary = result.get("predicted_salary")
            
            st.success(f"### Offer : ${predicted_salary:,.2f}")
            st.balloons()
            
        elif response.status_code == 500:
            st.error("🚨 Backend Error: Ensure that `salary_model.pkl` has been downloaded from Google Colab and placed inside the `backend` folder!")
        else:
            st.error(f"Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        st.error("🚨 Connection Failed! Is the FastAPI backend running on port 8000?")

st.markdown("---")
