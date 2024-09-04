import streamlit as st
import pandas as pd
from ntscraper import Nitter
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle
import re
import time  

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

# Streamlit UI - Title and Input Field
st.title('Real-Time Twitter Data with Disaster Prediction')
st.write('Enter a hashtag to scrape related tweets in real-time.')

# User input for hashtag
hashtag = st.text_input("Hashtag")

# If the user has entered a hashtag
if hashtag:
    # Specify the Nitter instance URL
    nitter_instance_url = "https://nitter.lucabased.xyz"

    # Initialize the scraper
    scraper = Nitter(nitter_instance_url)

    # DataFrame to store tweets and predictions
    tweets_df = pd.DataFrame(columns=['twitter_link', 'text', 'date', 'prediction'])

    # Start a loop to scrape tweets
    st.write("Fetching tweets... (Press Ctrl+C to stop)")
    while True:
        # Get tweets with the user-specified hashtag
        tweets = scraper.get_tweets(hashtag, mode='hashtag', number=10)

        # Create a temporary list to hold new rows
        new_rows = []

        # Process and classify each tweet
        for x in tweets['tweets']:
            tweet_link = x['link']
            tweet_text = x['text']
            tweet_date = x['date']
            
            # Preprocess the tweet text
            processed_text = preprocess_text(tweet_text)

            # Convert text to sequences
            sequence = tokenizer.texts_to_sequences([processed_text])
            
            # Pad sequences
            padded_sequence = pad_sequences(sequence, maxlen=max_len)
            
            # Make prediction
            prediction = model.predict(padded_sequence)[0][0]
            prediction_label = "Disaster" if prediction > 0.5 else "Non-Disaster"

            # Append new row to the temporary list
            new_rows.append({
                'twitter_link': tweet_link,
                'text': tweet_text,
                'date': tweet_date,
                'prediction': prediction_label
            })

        # Convert the new rows to a DataFrame
        new_tweets_df = pd.DataFrame(new_rows)

        # Concatenate the new tweets with the existing DataFrame
        tweets_df = pd.concat([tweets_df, new_tweets_df], ignore_index=True)

        # Display the DataFrame in Streamlit
        st.dataframe(tweets_df)

        # Sleep for a while before fetching new tweets
        time.sleep(30)  # Adjust the sleep time as necessary
else:
    st.write("Please enter a hashtag to see results.")

