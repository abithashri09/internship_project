import pandas as pd
import os

# -----------------------------
# Load analyzed data
# -----------------------------
file_path = "data/analyzed_stock_data.csv"

if not os.path.exists(file_path):
    raise FileNotFoundError("analyzed_stock_data.csv not found.")

df = pd.read_csv(file_path)

# -----------------------------
# Latest data for each stock
# -----------------------------
latest = (
    df.sort_values("Date")
      .groupby("Ticker", as_index=False)
      .last()
)

# -----------------------------
# KPIs
# -----------------------------
top_gainer = latest.loc[latest["Daily Return (%)"].idxmax()]
top_loser = latest.loc[latest["Daily Return (%)"].idxmin()]

average_close = latest["Close"].mean()

total_volume = latest["Volume"].sum()

# -----------------------------
# AI Summary
# -----------------------------
summary = f"""
======================================================
📈 AI STOCK MARKET SUMMARY
======================================================

🏆 Top Gainer
{top_gainer['Ticker']}
Daily Return : {top_gainer['Daily Return (%)']:.2f} %

------------------------------------------------------

📉 Top Loser
{top_loser['Ticker']}
Daily Return : {top_loser['Daily Return (%)']:.2f} %

------------------------------------------------------

💰 Average Closing Price

${average_close:.2f}

------------------------------------------------------

📦 Total Trading Volume

{int(total_volume):,}

------------------------------------------------------

🤖 AI Market Insight

• The market displayed mixed performance across sectors.

• {top_gainer['Ticker']} showed the strongest daily momentum.

• {top_loser['Ticker']} experienced the largest decline.

• High trading volumes indicate active investor participation.

• Monitoring moving averages and daily returns helps identify short-term market trends.

======================================================
"""

print(summary)

# Save summary
with open("data/ai_summary.txt", "w") as file:
    file.write(summary)

print("✅ AI Summary saved to data/ai_summary.txt")