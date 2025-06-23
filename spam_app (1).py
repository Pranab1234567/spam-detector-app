
import streamlit as st
import joblib

st.title("📧 Email Spam Classifier")

model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("spam_vectorizer.pkl")

msg = st.text_area("Enter your email or message here")

if st.button("Check"):
    vec = vectorizer.transform([msg])
    result = model.predict(vec)[0]
    if result == 1:
        st.error("⚠️ This message is SPAM!")
    else:
        st.success("✅ This message is NOT spam.")
