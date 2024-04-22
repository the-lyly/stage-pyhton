import streamlit as st
import joblib

# Load the trained logistic regression model
knn = joblib.load('MRknn_model.joblib')

# Streamlit webpage title
st.title('Fraud Detection Model Deployment')

# Input features into the model
def user_input_features():
    feature_1 = st.number_input('wilaya')
    feature_2 = st.number_input('BP')
    # Add as many features as you need
    # ...
    return [feature_1, feature_2]

st.subheader('User Input Features')
input_data = user_input_features()

# When 'Predict' button is clicked, make a prediction and display it
if st.button('Predict'):
    prediction = log_reg.predict([input_data])
    st.write(f'Prediction: {prediction[0]}')

# Add additional instructions and information as needed
