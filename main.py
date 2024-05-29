import streamlit as st
from transformers import pipeline

# Load the sentiment analysis pipeline with a specified model and revision
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
revision = "af0f99b"
classifier = pipeline("sentiment-analysis", model=model_name, revision=revision)

# Streamlit application
st.set_page_config(page_title="SentimentScope", layout="centered")

st.markdown(
    """
    <style>
    .main {
        background-color: #4B4E6C;
        padding: 10px;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: black;
        color: grey;
        text-align: center;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar navigation
st.sidebar.title("Navigation")
selected = st.sidebar.radio("Go to", ["Home", "Contact Me"])

if selected == "Home":
    st.title("SentimentScope")
    st.write("Enter some text to analyze its sentiment.")

    # Text input
    user_input = st.text_area("Your text here", height=150)

    if st.button("Analyze"):
        if user_input:
            with st.spinner("Analyzing..."):
                result = classifier(user_input)
                sentiment = result[0]['label']
                score = result[0]['score'] * 100  # Convert to percentage

                if sentiment == 'POSITIVE':
                    st.success(f"Sentiment: {sentiment} (Confidence: {score:.2f}%)")
                else:
                    st.error(f"Sentiment: {sentiment} (Confidence: {score:.2f}%)")
        else:
            st.warning("Please enter some text to analyze.")

elif selected == "Contact Me":
    st.header("Contact Me")
    st.write("Please fill out the form below to get in touch with me.")

    # Input fields for user's name, email, and message
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message", height=150)

    # Submit button
    if st.button("Submit"):
        if name.strip() == "" or email.strip() == "" or message.strip() == "":
            st.warning("Please fill out all the fields.")
        else:
            # Placeholder for email sending functionality
            send_email_to = 'kumawatharsh2004@email.com'
            st.success("Your message has been sent successfully!")

# Footer
footer = """
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://www.linkedin.com/in/harsh-kumawat-069bb324b/" target="_blank">Harsh</a></p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

# Adding an image
# st.sidebar.image("https://via.placeholder.com/150", caption="SentimentScope Logo")
