import streamlit as st
import twint
import pandas as pd
import json
import botocore

from tweety.bot import Twitter
app = Twitter()
st.subheader("""
Let's scrape some Tweets... Hope Twitter doesn't ban me :smile:
""")
search_term = st.text_input('What do you want to search for?')
all_tweets = app.get_tweets(search_term)

for tweet in all_tweets:
  #st.write(tweet)
  st.write(tweet[id], tweet[text], tweet[created_on])




  
