import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def predict_stock(data):
    if 'Close' not in data.columns or len(data) < 2:
        return [0] * len(data)

    data = data.reset_index()
    data['Date_Ordinal'] = pd.to_datetime(data['Date']).map(pd.Timestamp.toordinal)

    X = data['Date_Ordinal'].values.reshape(-1, 1)
    y = data['Close'].values

    model = LinearRegression()
    model.fit(X, y)
    predicted = model.predict(X)

    return predicted
