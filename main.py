from textblob import TextBlob
import pandas as pd
import streamlit as st
from textblob import TextBlob
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk


st.caption('redder_rider')
image = Image.open('emotion.png')
st.image(image)
st.header('Sentiment Analysis')
with st.text('Analyze Text'):
    text = st.text_input("Enter your POV to check it's polarity:")
    if text:
        blob = TextBlob(text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))

    nltk.download("vader_lexicon")
    s = SentimentIntensityAnalyzer()
    score = s.polarity_scores(text)

if score == 0:
        st.write("")
elif score["neg"] != 0:
        st.write("# Negative POV 😞")
elif score["pos"] != 0:
        st.write("# Positive POV 🙂")

# else :
#     st.write("# Neutral POV 😐")


with st.expander('Analyze xlsx'):
    upl = st.file_uploader('Upload file')

    def score(x):
        blob1 = TextBlob(x)
        return blob1.sentiment.polarity

    def analyze(x):
        if x >= 0.5:
            return 'Positive'
        elif x <= -0.5:
            return 'Negative'
        else:
            return 'Neutral'

    if upl:
        df = pd.read_excel(upl)
        del df['Unnamed: 0']
        df['score'] = df['Reviews'].apply(score)
        df['analysis'] = df['score'].apply(analyze)
        st.write(df.head(10))

        @st.cache
        def convert_df(df):

            return df.to_csv().encode('utf-8')

        csv = convert_df(df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='sentiment.csv',
            mime='text/csv',
        )





