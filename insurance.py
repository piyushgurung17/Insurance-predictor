import streamlit as st
import pickle as pk
import numpy as np

# Load model
model = pk.load(open('insurance.pickle', 'rb'))

# App title and header image
st.set_page_config(page_title="Insurance Prediction System", layout="centered")
st.title('🩺 Insurance Expense Prediction System')
st.image('https://www.shutterstock.com/image-vector/insurance-web-header-banner-covers-260nw-1122038591.jpg')

# Section header
st.markdown("### 📝 Enter your details below")

# Input fields using columns
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("🎂 Age", min_value=20, max_value=70, value=25)
with col2:
    bmi = st.number_input("⚖️ BMI (Body Mass Index)", min_value=10.0, max_value=50.0, value=22.0)

smoke = st.radio('🚬 Do you smoke?', ['Yes', 'No'], index=1)
smoke = 1 if smoke == 'Yes' else 0

region = st.selectbox('🌍 Select your region', ['Southeast', 'Southwest', 'Northeast', 'Northwest'])

# One-hot encoding for region
southeast = 1 if region == 'Southeast' else 0
southwest = 1 if region == 'Southwest' else 0
northeast = 1 if region == 'Northeast' else 0
northwest = 1 if region == 'Northwest' else 0

# Prediction
if st.button('🔍 Predict Insurance Expense'):
    input_data = [[age, bmi, smoke, southeast]]
    predicted_expense = model.predict(input_data)
    st.success('✅ Data submitted successfully!')
    st.success(f'💰 Estimated Insurance Expense: **${predicted_expense[0]:.2f}**')
    st.balloons()
