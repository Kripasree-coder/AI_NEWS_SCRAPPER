import streamlit as st
import time
import plotly.express as px
import pandas as pd
from crypto_data import get_crypto_prices, get_historical_data
from config import CRYPTO_LIST, REFRESH_TIME

def display_live_prices():
    """Displays real-time crypto prices."""
    st.subheader("💰 Live Prices")
    placeholder = st.empty()

    if "prices" not in st.session_state:
        st.session_state["prices"] = {}

    while True:
        prices = get_crypto_prices()
        with placeholder.container():
            cols = st.columns(len(CRYPTO_LIST))
            for i, crypto in enumerate(CRYPTO_LIST):
                if crypto in prices:
                    price = prices[crypto]["usd"]
                    market_cap = prices[crypto].get("usd_market_cap", "N/A")

                    # Color for price changes
                    change_color = "green" if price > st.session_state["prices"].get(crypto, price) else "red"
                    st.session_state["prices"][crypto] = price

                    with cols[i]:
                        st.metric(
                            label=f"📌 {crypto.capitalize()}",
                            value=f"${price:,.2f}",
                            delta=f"Market Cap: ${market_cap:,.0f}",
                            delta_color="normal" if price > st.session_state["prices"].get(crypto, price) else "inverse"
                        )

        time.sleep(REFRESH_TIME)
        st.rerun()  # Fix for auto-refresh (Replaces experimental_rerun)

def display_crypto_trend():
    """Displays crypto price trends as a line chart."""
    st.subheader("📊 7-Day Price Trends")

    for crypto in CRYPTO_LIST:
        data = get_historical_data(crypto)
        prices = data.get("prices", [])
        if prices:
            df = pd.DataFrame(prices, columns=["timestamp", "price"])
            df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

            fig = px.line(df, x="timestamp", y="price",
                          title=f"📈 {crypto.capitalize()} Price Trends",
                          labels={"timestamp": "Date", "price": "Price (USD)"},
                          line_shape="spline",
                          markers=True)
            st.plotly_chart(fig, use_container_width=True)

def display_about_section():
    """Displays About & Credits Section."""
    st.sidebar.markdown("---")
    st.sidebar.markdown("👨‍💻 **Developed by: Kripa**")
    st.sidebar.markdown("[🌐 GitHub](https://github.com/Kripasree-coder)")
    st.sidebar.markdown("[💼 LinkedIn](https://www.linkedin.com/in/kripa-sree-m/)")
