# Sentiment Analysis Project

This project is a sentiment analysis application that predicts the sentiment of a given text input using NLP techniques. It is built using the NLTK library and trained with a Bag of Words algorithm. The application is deployed using Streamlit and can be accessed [here](https://senti-analysis-by-raj.streamlit.app/).

## Features

- **Sentiment Analysis**: Predicts whether the input text is positive or negative.
- **User-friendly Interface**: Built with Streamlit for easy interaction.
- **Deployed Online**: Accessible via a web browser.

## Demo

You can try out the application live [here](https://senti-analysis-by-raj.streamlit.app/).

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/senti-analysis-by-rj
    cd YourRepositoryName
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Streamlit app**:
    ```bash
    streamlit run streamlit_app.py
    ```

## Usage

1. Open the Streamlit app in your web browser (usually `http://localhost:8501`).
2. Enter a text input in the provided field.
3. Click the "Analyze" button to see the sentiment prediction.

## Dependencies

- Python 3.6+
- Streamlit
- NLTK
- Pandas

Ensure all dependencies are installed by running:
```bash
pip install -r requirements.txt
```
#Made with ❤️ by RAJ
