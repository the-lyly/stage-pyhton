import streamlit as st
import joblib
import numpy as np

# Load your trained KNN model
knn = joblib.load('MRknn_model.joblib')

# Define the structure of your web app
st.title('KNN Model Deployment for Fraud Detection')
st.write('Please enter the required information to predict the fraud status:')

# Assuming 'feature' is the name of the feature used by your KNN model
feature_input = st.number_input('Feature Input (Difference between ChAff and Total TVA annuelle)', value=0.0)

# When 'Predict' is clicked, make a prediction and display it
if st.button('Predict'):
    # Note: Ensure that the input is in the same format as your model expects
    prediction = knn.predict(np.array([[feature_input]]))
    
    # Convert prediction to meaningful output
    if prediction == 0:
        result = 'Bon (No Fraud Detected)'
    elif prediction == 1:
        result = 'Suspected Fraud'
    elif prediction == 2:
        result = 'Fraud Detected'
    else:
        result = 'Unknown Category'
    
    st.write(f'The prediction is: {result}')
