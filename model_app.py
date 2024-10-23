import streamlit as st
import joblib

# Load the model
model = joblib.load('regression.joblib')

# Set up the Streamlit app
st.title('House Price Prediction')

# Create input fields
size = st.number_input('House Size ', min_value=0.0, step=100.0)
bedrooms = st.number_input('Number of Bedrooms', min_value=0, step=1)
has_garden = st.selectbox('Has Garden', ['No', 'Yes'])

# Convert 'Has Garden' to binary
has_garden_binary = 1 if has_garden == 'Yes' else 0

# Make prediction when the user clicks the button
if st.button('Predict Price'):
    # Prepare the input data
    input_data = [[size, bedrooms, has_garden_binary]]
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display the result
    st.write(f'Predicted House Price: ${prediction[0]:,.2f}')