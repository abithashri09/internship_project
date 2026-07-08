import os
import pandas as pd

# -------------------------------
# Load Data
# -------------------------------

input_file = "data/stocks.csv"

if not os.path.exists(input_file):
    raise FileNotFoundError("data/stocks.csv not found.")

df = pd.read_csv(input_file)

# -------------------------------
# Convert Date
# -------------------------------

df["Date"] = pd.to_datetime(df["Date"])

# -------------------------------
# Sort Data
# -------------------------------

df = df.sort_values(["Ticker", "Date"])

# -------------------------------
# Daily Return
# -------------------------------

df["Daily Return (%)"] = (
    ((df["Close"] - df["Open"]) / df["Open"]) * 100
).round(2)

# -------------------------------
# Moving Average
# -------------------------------

df["MA5"] = (
    df.groupby("Ticker")["Close"]
      .transform(lambda x: x.rolling(5).mean())
)

df["MA10"] = (
    df.groupby("Ticker")["Close"]
      .transform(lambda x: x.rolling(10).mean())
)

# -------------------------------
# Latest Record Per Stock
# -------------------------------

latest = (
    df.sort_values("Date")
      .groupby("Ticker", as_index=False)
      .last()
)

# -------------------------------
# KPIs
# -------------------------------

top_gainer = latest.loc[latest["Daily Return (%)"].idxmax()]
top_loser = latest.loc[latest["Daily Return (%)"].idxmin()]

average_close = round(latest["Close"].mean(), 2)

total_volume = int(latest["Volume"].sum())

# -------------------------------
# Display Results
# -------------------------------

print("\n==============================")
print("AI STOCK MARKET ANALYSIS")
print("==============================")

print(f"\n🏆 Top Gainer : {top_gainer['Ticker']}")
print(f"Daily Return : {top_gainer['Daily Return (%)']} %")

print(f"\n📉 Top Loser : {top_loser['Ticker']}")
print(f"Daily Return : {top_loser['Daily Return (%)']} %")

print(f"\n💰 Average Closing Price : ${average_close}")

print(f"\n📦 Total Volume : {total_volume:,}")

# -------------------------------
# Save File
# -------------------------------

os.makedirs("data", exist_ok=True)

df.to_csv(
    "data/analyzed_stock_data.csv",
    index=False
)

print("\n✅ analyzed_stock_data.csv created successfully.")