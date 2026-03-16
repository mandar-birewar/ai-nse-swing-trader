import ta

def add_indicators(df):

    df["rsi"] = ta.momentum.RSIIndicator(df["Close"]).rsi()

    df["macd"] = ta.trend.MACD(df["Close"]).macd()

    df["ma20"] = df["Close"].rolling(20).mean()

    df["ma50"] = df["Close"].rolling(50).mean()

    df["volume"] = df["Volume"]

    return df