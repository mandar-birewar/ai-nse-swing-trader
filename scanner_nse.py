import pandas as pd
import joblib

from indicators import add_indicators
from telegram_alert import send_message

model = joblib.load("model.pkl")

stocks = open("stocks.txt").read().splitlines()

features = ["rsi","macd","ma20","ma50","volume"]

signals = []

for stock in stocks:

    try:

        df = pd.read_csv(f"data/{stock}.csv")

        df = add_indicators(df)

        df = df.dropna()

        latest = df.tail(1)

        pred = model.predict(latest[features])[0]

        prob = model.predict_proba(latest[features])[0][1]

        if pred == 1:

            price = latest["Close"].values[0]

            entry = round(price * 0.995,2)
            target = round(price * 1.05,2)
            stop = round(price * 0.97,2)

            confidence = round(prob*100,2)

            signals.append(
                (stock, entry, target, stop, confidence)
            )

    except:
        continue


signals = sorted(signals, key=lambda x: x[4], reverse=True)

top = signals[:5]

if len(top) == 0:

    send_message("No swing trades today.")

else:

    message = "🔥 AI Swing Trade Signals 🔥\n\n"

    for s in top:

        message += f"""
{s[0]}

Buy: {s[1]}
Target: {s[2]}
Stop Loss: {s[3]}
Confidence: {s[4]}%

"""

    send_message(message)

print("Scan complete")