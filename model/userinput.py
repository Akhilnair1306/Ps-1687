import streamlit as st
import pandas as pd
from ntscraper import Nitter

# Streamlit UI - Title and Input Field
st.title('Twitter Data')
st.write('Enter a hashtag to scrape related tweets.')

# User input for hashtag
hashtag = st.text_input("Hashtag")

# If the user has entered a hashtag
if hashtag:
    # Specify the Nitter instance URL
    nitter_instance_url = "https://nitter.lucabased.xyz"

    # Initialize the scraper
    scraper = Nitter(nitter_instance_url)

    # Get tweets with the user-specified hashtag
    tweets = scraper.get_tweets(hashtag, mode='hashtag', number=10)

    # Prepare the data
    final_tweets = []
    for x in tweets['tweets']:
        data = [x['link'], x['text'], x['date']]
        final_tweets.append(data)

    # Create a DataFrame
    dat = pd.DataFrame(final_tweets, columns=['twitter_link', 'text', 'date'])

    # Display the DataFrame in Streamlit
    st.dataframe(dat)

    # Alternatively, you can use st.table(dat) if you prefer a static table.
else:
    st.write("Please enter a hashtag to see results.")


