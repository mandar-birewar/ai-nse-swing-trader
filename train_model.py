import pandas as pd
import os
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from indicators import add_indicators

os.makedirs("data", exist_ok=True)

dataset = []

for file in os.listdir("data"):

    df = pd.read_csv(f"data/{file}")

    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
    df["Open"] = pd.to_numeric(df["Open"], errors="coerce")
    df["High"] = pd.to_numeric(df["High"], errors="coerce")
    df["Low"] = pd.to_numeric(df["Low"], errors="coerce")
    df["Volume"] = pd.to_numeric(df["Volume"], errors="coerce")

    df = add_indicators(df)

    df["future_price"] = df["Close"].shift(-5)

    df["target"] = (df["future_price"] > df["Close"] * 1.03).astype(int)

    df = df.dropna()

    dataset.append(df)

data = pd.concat(dataset)

features = ["rsi","macd","ma20","ma50","volume"]

X = data[features]
y = data["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

model = RandomForestClassifier(n_estimators=300)

model.fit(X_train, y_train)

print("Model Accuracy:", model.score(X_test,y_test))

joblib.dump(model,"model.pkl")
