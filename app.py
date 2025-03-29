import streamlit as st
import pandas as pd
from news_scraper import fetch_headlines, summarize_text

st.set_page_config(page_title="AI News Scraper", page_icon="📰", layout="wide")
st.title("📰 AI News Scraper & Summarizer")

if st.button("Fetch Latest AI News"):
    with st.spinner("Fetching AI news..."):
        headlines = fetch_headlines()
        summarized = [summarize_text(headline) for headline in headlines]
        
        df = pd.DataFrame({"Original Headlines": headlines, "Summarized": summarized})
        st.dataframe(df, use_container_width=True)

        df.to_csv("news_headlines.csv", index=False)
        st.success("✅ News fetched & saved successfully!")
