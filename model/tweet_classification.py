# streamlit_app.py

import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences  # Change made here
import numpy as np
import pickle
import re  # Importing the re module for regular expressions

# Load the saved model
model = tf.keras.models.load_model('disaster_prediction_model.h5')

# Load the tokenizer used during training
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

max_len = 100  # The max length used during training

# Define preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'[^\w\s]', '', text)
    text = " ".join([word for word in text.split()])
    return text

# Streamlit app interface
st.title('Disaster Tweet Prediction')

user_input = st.text_area("Enter a tweet text to predict if it's a disaster or not")

if st.button('Predict'):
    # Preprocess the input text
    processed_text = preprocess_text(user_input)
    
    # Convert text to sequences
    sequence = tokenizer.texts_to_sequences([processed_text])
    
    # Pad sequences
    padded_sequence = pad_sequences(sequence, maxlen=max_len)
    
    # Make prediction
    prediction = model.predict(padded_sequence)[0][0]
    
    if prediction > 0.5:
        st.write("This tweet is classified as a **Disaster** tweet.")
    else:
        st.write("This tweet is classified as a **Non-Disaster** tweet.")
