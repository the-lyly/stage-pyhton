import streamlit as st
import joblib
import numpy as np

# Load your trained KNN model
model = joblib.load('MRknn_model.joblib')

st.title('Fraud Detection Prediction')

# Input field for the user to enter the BP
bp_input = st.text_input('Enter Business Partner ID (BP):', '')

# Predict button
if st.button('Predict'):
    try:
        # Convert input to int (or leave as str if the model expects that)
        bp_value = int(bp_input)
        
        # The model expects a 2D array as input, so we reshape the input accordingly
        bp_value_reshaped = np.array(bp_value).reshape(-1, 1)
        
        # Make the prediction
        prediction = model.predict(bp_value_reshaped)
        
        # Output the prediction (assuming the output is binary or categorical)
        prediction_mapping = {0: 'Non-Fraud', 1: 'Fraud', 2: 'Suspect'}
        st.write(f'The model prediction for BP {bp_input} is: {prediction_mapping[prediction[0]]}')
    except ValueError:
        st.error('Please enter a valid BP number.')
