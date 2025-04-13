from textblob import TextBlob
import streamlit as st

st.title("Product Review Sentiment Analyzer")

review = st.text_area("Enter the product review:")

if st.button("Analyze"):
    blob = TextBlob(review)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        st.success("Positive Sentiment")
    elif sentiment < 0:
        st.error("Negative Sentiment")
    else:
        st.info("Neutral Sentiment")