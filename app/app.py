import streamlit as st
import joblib
from sklearn.feature_extraction.text import CountVectorizer
import streamlit as st
import joblib

# Load trained model
loaded_model = joblib.load(r'model\\my_model.joblib')

# Load SAME vectorizer
countvectorizer = joblib.load(r'model\\vectorizer.joblib')

if loaded_model:
    st.success('Model loaded')

st.title('news classifier')
st.write('classify news by its heading')

inp = st.text_input('Enter input')

if inp:   # input empty na ho
    inp_vectorizer = countvectorizer.transform([inp]) 
    prediction = loaded_model.predict(inp_vectorizer)

    st.write('Your input:', inp)
    st.write('Prediction:', prediction[0])