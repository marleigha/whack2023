import streamlit as st
import pandas as pd
import numpy as np
from streamlit_card import card
#importing the pieces streamlit had in their script

#title is pending
st.title('CultureAtlas')
st.subheader('presented by team rocket!')

#fetch data
DATE_COLUMN = 'date/time'
DATA_URL = ('data url')

#downloads data + converts the data column from text to datetime
#nrow = num of rows we want to load into dataframe
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

inputCultures = [];
inputCultures.append("French")
#options = st.selectbox(
   #'What Culture Are you Looking to Attend Events For?',
   #['Native American', 'Japanese', 'Kenyan', 'Irish', 'Chinese','French'])
options = st.selectbox(
   'What Culture Are you Looking to Attend Events For?',
   inputCultures)
inputCultures.append('Korean')

st.write("Here are some events celebrating ", options, " culture")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")