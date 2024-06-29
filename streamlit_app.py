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
    """Loads the sentiment analysis model from the pickle file (sia.pkl).

    Returns:
        object: The loaded sentiment analysis model.
    """

    with open('sia.pkl', 'rb') as f:
        sia_model = pickle.load(f)
    return sia_model

def main():
    """Main function to handle Streamlit app interactions."""

    st.title("Sentiment Analysis🎭")

    user_input = st.text_input("Enter something NEGATIVE or POSITIVE to analyze:")

    if user_input:
        sia_model = load_sentiment_model()  # Load model only when needed
        prediction = predict_sentiment(user_input, sia_model)
        st.write(f"Sentiment: {prediction}")

    # Footer
    st.markdown("---")
    st.markdown("Made with ❤️ by RAJ")

if __name__ == '__main__':
    main()
