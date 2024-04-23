import streamlit as st
import joblib
import numpy as np
import pandas as pd
import plotly.express as px

# Load your trained KNN model
model = joblib.load('MRknn_model.joblib')

# Load the dataset
@st.cache  # Use Streamlit's caching to load the data only once
def load_data():
    return pd.read_excel('graphesdf.xlsx')

df = load_data()

# Calculate the percentage of fraud by Wilaya
fraud_by_wilaya = df[df['cible'] == 'fraude'].groupby('Wilaya')['cible'].count() / df.groupby('Wilaya')['cible'].count()
fraud_by_wilaya = fraud_by_wilaya.reset_index().rename(columns={'cible': 'Fraud Percentage'})

# Calculate the percentage of fraud by Code CNRC
fraud_by_cnrc = df[df['cible'] == 'fraude'].groupby('Code CNRC')['cible'].count() / df.groupby('Code CNRC')['cible'].count()
fraud_by_cnrc = fraud_by_cnrc.reset_index().rename(columns={'cible': 'Fraud Percentage'})

# Streamlit app
st.title('Fraud Detection Prediction and Analysis')

# Input field for the user to enter the BP
bp_input = st.text_input('Enter Business Partner ID (BP):', '')

# Predict button
if st.button('Predict'):
    try:
        bp_value = int(bp_input)
        bp_value_reshaped = np.array(bp_value).reshape(-1, 1)
        prediction = model.predict(bp_value_reshaped)
        prediction_mapping = {0: 'Non-Fraud', 1: 'Fraud', 2: 'Suspect'}
        st.write(f'The model prediction for BP {bp_input} is: {prediction_mapping[prediction[0]]}')
    except ValueError:
        st.error('Please enter a valid BP number.')

# Interactive graph of Fraud Percentage by Wilaya
st.subheader('Fraud Percentage by Wilaya')
fig_wilaya = px.bar(fraud_by_wilaya, x='Wilaya', y='Fraud Percentage')
st.plotly_chart(fig_wilaya)

# Interactive graph of Fraud Percentage by Code CNRC
st.subheader('Fraud Percentage by Code CNRC')
fig_cnrc = px.bar(fraud_by_cnrc, x='Code CNRC', y='Fraud Percentage')
st.plotly_chart(fig_cnrc)
