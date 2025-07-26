import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from predict import predict_stock  # Make sure predict.py is in the same directory

st.title("📈 Stock Price Predictor")

# Load the symbol list
try:
    df_symbols = pd.read_csv("nse_stocks.csv")  # Make sure the CSV exists and has Symbol,Name columns
    symbols = df_symbols['Symbol'].tolist()
    names = df_symbols['Name'].tolist()
    symbol_name_map = dict(zip(names, symbols))
except Exception as e:
    st.error("Failed to load symbol list. Make sure 'nse_stocks.csv' exists and has columns 'Symbol' and 'Name'.")
    st.stop()

# Dropdown to select company
company = st.selectbox("Select a Company", names)

# Get symbol from name
symbol = symbol_name_map[company]

# Date input
st.write("Select time period for stock data:")
start_date = st.date_input("Start date", pd.to_datetime("2022-01-01"))
end_date = st.date_input("End date", pd.to_datetime("2023-01-01"))

# Fetch data button
if st.button("Fetch & Predict"):
    st.info(f"Fetching data for {symbol} from {start_date} to {end_date}")
    try:
        data = yf.download(symbol, start=start_date, end=end_date)
        if data.empty:
            st.warning("No data found for this range. Try different dates.")
            st.stop()

        st.subheader("📊 Historical Close Price")
        st.line_chart(data['Close'])

        st.subheader("🔮 Predicted Prices")
        predicted_prices = predict_stock(data)

        # Plot actual vs predicted
        plt.figure(figsize=(12, 6))
        plt.plot(data.index, data['Close'], label='Actual Price')
        plt.plot(data.index, predicted_prices, label='Predicted Price', linestyle='--')
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        st.pyplot(plt)

    except Exception as e:
        st.error(f"Error fetching or predicting data: {e}")
