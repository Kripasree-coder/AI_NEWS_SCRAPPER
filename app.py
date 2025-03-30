import streamlit as st
from ui_components import display_live_prices, display_crypto_trend, display_about_section

# Set Page Config
st.set_page_config(page_title="Crypto Dashboard", page_icon="🚀", layout="wide")

# Sidebar Navigation
st.sidebar.title("🚀 Crypto Dashboard")
st.sidebar.write("📌 Track live prices & trends of your favorite cryptocurrencies.")
display_about_section()
st.sidebar.markdown("---")

# Sections
st.title("📈 Live Cryptocurrency Tracker")
display_live_prices()   # Live Price Dashboard
display_crypto_trend()  # Crypto Trends


