# 📈 Stock Price Prediction using Linear Regression

This project demonstrates how to predict stock prices of Indian companies listed on the NSE (National Stock Exchange) using **Linear Regression**. The app fetches historical stock data and projects the next 30 days of stock prices based on a trained regression model.

---

## 🚀 Features

- ✅ User can input company name (e.g., TCS, Reliance, HDFC).
- 🔍 Matches the company and fetches historical data using **Yahoo Finance (yfinance)**.
- 📊 Uses **Linear Regression** to forecast the next 30 business days' stock prices.
- 📈 Displays interactive prediction charts using **Matplotlib** or **Streamlit**.
- 🧠 Model is simple and educational (ideal for beginners in ML/finance).

---

## 🗂️ Project Structure

Stock-Price-Prediction-using-Linear-Regression/
│
├── app.py # Streamlit web app
├── predict.py # Console-based prediction script
├── nse_stocks.csv # List of NSE companies and symbols (Symbol, Name)
├── requirements.txt # Python dependencies
└── README.md # Project description

yaml
Copy
Edit

---

## 🛠️ How to Run

### ✅ 1. Clone the Repository
```bash
git clone https://github.com/urvish2930/Stock-Price-Predication-using-Linear-Regression.git
cd Stock-Price-Predication-using-Linear-Regression

✅ 2. Install Dependencies
   pip install -r requirements.txt

✅ 3. Run the Console App
      python predict.py

📦 Requirements
Python 3.8+
pandas
numpy
yfinance
matplotlib
scikit-learn


Install all using:
pip install -r requirements.txt

📘 How it Works
User enters a company name (e.g., tcs, reliance).

We match the name with nse_stocks.csv to fetch the NSE ticker (e.g., TCS.NS).

- Historical data is pulled from Yahoo Finance.
- A Linear Regression model fits past data and predicts the next 30 days.
- Results are shown in a simple line chart.


🧑‍💻 Author
Urvish Pandya
📫 GitHub

📄 License
This project is open-source and available under the MIT License.

⭐ If you like this project, don't forget to star the repo!
