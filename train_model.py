import yfinance as yf
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from indicators import add_indicators

print("Starting model training...")

stocks = open("stocks.txt").read().splitlines()

dataset = []

for stock in stocks[:120]:

    try:

        df = yf.download(stock, period="1y", progress=False)

        if df is None or df.empty:
            continue

        df = add_indicators(df)

        df["future_price"] = df["Close"].shift(-5)
        df["target"] = (df["future_price"] > df["Close"] * 1.02).astype(int)

        df = df.dropna()

        if len(df) < 30:
            continue

        dataset.append(df)

        print("Loaded:", stock)

    except Exception as e:

        print("Skipped:", stock)

# ---------- SAFE TRAINING ----------
if len(dataset) == 0:

    print("No training data found. Creating fallback dataset.")

    data = pd.DataFrame({
        "rsi":[50,60,40,55,45,65],
        "macd":[0.1,0.2,-0.1,0.05,-0.05,0.15],
        "ma20":[100,102,98,101,97,104],
        "ma50":[99,101,97,100,96,103],
        "volume":[1000,1200,900,1100,950,1300],
        "target":[1,0,1,0,1,0]
    })

else:

    data = pd.concat(dataset, ignore_index=True)

features = ["rsi","macd","ma20","ma50","volume"]

X = data[features]
y = data["target"]

model = RandomForestClassifier(n_estimators=200, random_state=42)

model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model trained successfully")