import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fetch_data(company):
    ticker = f"{company.upper()}.NS"
    print(f"✅ Fetching stock data for {ticker}...")
    try:
        data = yf.download(ticker, start="2022-01-01", end="2024-12-31")
        if data.empty:
            print("❌ No data found for this ticker.")
            return None
        return data
    except Exception as e:
        print("❌ Error fetching data:", e)
        return None

def predict_prices(data):
    data = data[['Close']].dropna()
    data.reset_index(inplace=True)
    data['Days'] = np.arange(len(data))

    X = data[['Days']]
    y = data['Close']

    model = LinearRegression()
    model.fit(X, y)

    future_days = 30
    future_X = np.arange(len(data), len(data) + future_days).reshape(-1, 1)
    future_preds = model.predict(future_X)

    return future_preds

def plot_predictions(data, future_preds, company_name):
    last_date = data.index[-1]
    future_dates = pd.date_range(start=last_date, periods=31, freq='B')[1:]  # 30 business days

    plt.figure(figsize=(10, 6))
    plt.plot(data['Close'], label="Historical Price")
    plt.plot(future_dates, future_preds, label="Predicted Price", linestyle='--')
    plt.title(f"Stock Price Prediction - {company_name.upper()}")
    plt.xlabel("Date")
    plt.ylabel("Price (INR)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    company = input("Enter company name: ").strip()
    data = fetch_data(company)

    if data is None:
        return

    future_preds = predict_prices(data)
    print("\n📈 Predicted Prices for next 30 days:")
    for i, price in enumerate(future_preds, 1):
        print(f"Day {i}: ₹{price.item():.2f}")

    plot_predictions(data, future_preds, company)

if __name__ == "__main__":
    main()
