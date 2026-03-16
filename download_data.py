import yfinance as yf
import os
from tqdm import tqdm

stocks = open("stocks.txt").read().splitlines()

os.makedirs("data", exist_ok=True)

print("Downloading stock data...\n")

for stock in tqdm(stocks):

    try:

        df = yf.download(stock, start="2018-01-01", progress=False)

        if not df.empty:
            df.to_csv(f"data/{stock}.csv")

    except:

        print("Error downloading:", stock)

print("\nDownload complete")