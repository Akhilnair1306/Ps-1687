import streamlit as st
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the TensorFlow model and tokenizer
model = load_model('disaster_tweet_model.h5')

with open('tokenizer.pkl', 'rb') as file:
    tokenizer = pickle.load(file)

# UI for prediction
st.title("Disaster Tweet Predictor")

tweet_input = st.text_area("Enter a tweet to analyze")

if st.button("Predict"):
    if tweet_input:
        # Preprocess the input tweet using the loaded tokenizer
        sequences = tokenizer.texts_to_sequences([tweet_input])
        padded_sequences = pad_sequences(sequences, maxlen=100)  # Use the same maxlen used during model training

        # Make prediction using the loaded model
        prediction = model.predict(padded_sequences)
        is_disaster = prediction[0][0] > 0.5  # Assuming the model outputs probabilities and class 1 indicates disaster

        # Display result
        if is_disaster:
            st.write("This tweet is likely about a disaster.")
        else:
            st.write("This tweet is not about a disaster.")