import streamlit as st
import pandas as pd
import time
from news_scrapper import fetch_headlines, summarize_text

st.set_page_config(page_title="AI News Scraper", page_icon="📰", layout="wide")
st.title("📰 AI News Scraper & Summarizer")

# Ask user for refresh interval
refresh_time = st.number_input("Set refresh time (in minutes):", min_value=1, max_value=60, value=10, step=1)
st.write(f"Fetching news every **{refresh_time} minutes**.")

# Fetch and display news
def fetch_and_display():
    st.write("Fetching latest AI news... 🔄")
    headlines = fetch_headlines()
    summarized = [summarize_text(headline) for headline in headlines]
    df = pd.DataFrame({"Original Headlines": headlines, "Summarized": summarized})
    st.dataframe(df, use_container_width=True)

    # Save to CSV
    df.to_csv("news_headlines.csv", index=False)
    st.success("✅ News fetched & saved successfully!")

# Run first fetch immediately
fetch_and_display()

# Auto-refresh every X minutes
while True:
    time.sleep(refresh_time * 60)  # Convert minutes to seconds
    fetch_and_display()
