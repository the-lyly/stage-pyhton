import streamlit as st

# Title of the app
st.title('My Streamlit App')

# Asking the user for input
user_input = st.text_input("Enter some text")

# Displaying the input back to the user
if user_input:
    st.write(f"You entered: {user_input}")
