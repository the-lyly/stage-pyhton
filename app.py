import streamlit as st
import joblib
import numpy as np

# Load your trained model (adjust the path as necessary)
model = joblib.load('MRknn_model.joblib')

# Title for the Streamlit app
st.title('KNN Model Prediction for Business Partner ID')

# User input for BP
bp_input = st.text_input('Enter Business Partner ID (BP):', '')

# Prediction button
if st.button('Predict'):
    # The input needs to be converted to the same format the model was trained on
    # Assuming the model expects a standardized or normalized BP value
    # Here you should apply the same preprocessing as you did for your training data
    # For the demonstration, we will convert the input to float and reshape for the model input
    bp_value = np.array(float(bp_input)).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(bp_value)
    
    # Display the prediction
    # You should map the numeric prediction back to the categorical label
    # Assuming the mapping is {0: 'Class A', 1: 'Class B', 2: 'Class C'}
    prediction_mapping = {0: 'Non fraude', 1: 'Fraude', 2: 'Cas Suspect'}
    st.write(f'The model prediction for BP {bp_input} is: {prediction_mapping[prediction[0]]}')
