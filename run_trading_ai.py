import os

print("Starting AI NSE Scanner...\n")

# Step 1 - Download latest data
print("Downloading stock data...")
os.system("python download_data.py")

# Step 2 - Run AI scanner
print("Running AI model scan...")
os.system("python scanner_nse.py")

print("Scan complete. Telegram alerts sent if signals found.")