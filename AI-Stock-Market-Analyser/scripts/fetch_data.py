import os
import pandas as pd
import yfinance as yf

# -----------------------------
# Create data folder
# -----------------------------
os.makedirs("data", exist_ok=True)

# -----------------------------
# List of Stocks
# -----------------------------
stocks = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "META",
    "TSLA", "NVDA", "NFLX", "AMD", "INTC",
    "IBM", "ORCL", "CRM", "ADBE", "QCOM",
    "CSCO", "AVGO", "JPM", "NKE", "DIS"
]

all_data = []

print("Downloading stock data...\n")

for ticker in stocks:

    print(f"Downloading {ticker}...")

    try:

        stock = yf.Ticker(ticker)

        df = stock.history(
            period="1mo",
            interval="1d",
            auto_adjust=True
        )

        if df.empty:
            print(f"No data for {ticker}")
            continue

        df = df.reset_index()

        # Keep only required columns
        df = df[[
            "Date",
            "Open",
            "High",
            "Low",
            "Close",
            "Volume"
        ]]

        df["Ticker"] = ticker

        # Arrange columns
        df = df[[
            "Date",
            "Ticker",
            "Open",
            "High",
            "Low",
            "Close",
            "Volume"
        ]]

        all_data.append(df)

    except Exception as e:
        print(f"{ticker}: {e}")

# -----------------------------
# Merge all stocks
# -----------------------------
final_df = pd.concat(all_data, ignore_index=True)

# Round prices
price_cols = ["Open", "High", "Low", "Close"]

for col in price_cols:
    final_df[col] = final_df[col].round(2)

# Convert volume to integer
final_df["Volume"] = final_df["Volume"].astype(int)

# Save CSV
final_df.to_csv(
    "data/stocks.csv",
    index=False
)

print("\n=================================")
print("Download Completed Successfully")
print("=================================")

print(final_df.head())

print("\nRows :", len(final_df))
print("Stocks :", final_df["Ticker"].nunique())