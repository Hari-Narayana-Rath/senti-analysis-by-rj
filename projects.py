import streamlit as st
import pickle
import pandas as pd

def predict_sentiment(text, sia_model):
    prediction = sia_model.polarity_scores(text)
    if prediction['pos'] > prediction['neg']:
        return "Positive 😁"
    else:
        return "Negative 😔"

def load_sentiment_model():
    with open('pk.pkl', 'rb') as f:
        sia_model = pickle.load(f)
    return sia_model

def display_projects():
    st.title("Sentiment Analysis🎭")
    user_input = st.text_input("Enter something NEGATIVE or POSITIVE to analyze:")
    if user_input:
        sia_model = load_sentiment_model()
        prediction = predict_sentiment(user_input, sia_model)
        st.write(f"Sentiment: {prediction}")
    st.markdown("---")
    st.markdown("Made with ❤️ by RAJ")
