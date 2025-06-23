# 📧 Spam Email Classifier – Streamlit App

A simple Machine Learning web app built with **NLP + Streamlit** to classify whether a message is **Spam** or **Not Spam**.

---

## 🚀 Live Demo

👉 [Click here to try the app on Streamlit](https://titanic-app-app-lks4cfdtbmh4ggutlasxyn.streamlit.app)  
*(Replace with your actual Streamlit Cloud link if different)*

---

## 🔍 About the Project

This project uses a **Naive Bayes classifier** trained on the classic **SMS Spam Collection Dataset**.  
Key features:

- Text Preprocessing using **TF-IDF Vectorization**
- Classification with **Multinomial Naive Bayes**
- Interactive prediction for custom messages
- Live app built with **Streamlit**
- Deployed using **Streamlit Cloud**

---

## 📦 Files Included

| File                | Description                                      |
|---------------------|--------------------------------------------------|
| `spam_app.py`       | Main Streamlit frontend app                      |
| `spam_model.pkl`    | Trained spam classification model                |
| `spam_vectorizer.pkl` | TF-IDF vectorizer used for input transformation |
| `requirements.txt`  | Python libraries required to run the app         |

---

## 🛠️ Tech Stack

- Python
- Pandas
- Scikit-learn
- Natural Language Processing (TF-IDF)
- Streamlit
- GitHub + Streamlit Cloud (for deployment)

---

## 💻 Run Locally (Optional)

```bash
# Clone the repo
git clone https://github.com/Pranab1234567/spam-detector-app.git

# Navigate to project
cd spam-detector-app

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run spam_app.py

---

## 👤 Author

**Pranab Mahalik**  
[GitHub](https://github.com/Pranab1234567) | [LinkedIn](https://www.linkedin.com/in/YOUR-LINKEDIN-ID)  
*(Update the LinkedIn link)*

---

## 🌟 Acknowledgements

- Dataset: [UCI SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- Inspired by real-world applications of **NLP + ML**
- Built as part of my 60-day ML learning journey 🚀
