import ta

def add_indicators(df):

    # RSI
    df["rsi"] = ta.momentum.RSIIndicator(df["Close"]).rsi()

    # MACD
    df["macd"] = ta.trend.MACD(df["Close"]).macd()

    # Moving averages
    df["ma20"] = df["Close"].rolling(20).mean()
    df["ma50"] = df["Close"].rolling(50).mean()

    # Bollinger Bands
    bb = ta.volatility.BollingerBands(df["Close"])
    df["bb_high"] = bb.bollinger_hband()
    df["bb_low"] = bb.bollinger_lband()

    # Volume
    df["volume"] = df["Volume"]

    return df