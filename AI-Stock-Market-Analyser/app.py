import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os


st.set_page_config(
    page_title="AI Stock Market Analyzer",
    page_icon="📈",
    layout="wide"
)

st.markdown("""
<style>

.main{
    background-color:#F5F7FA;
}

h1,h2,h3{
    color:#1F2937;
}

[data-testid="stSidebar"]{
    background-color:#111827;
}

[data-testid="stSidebar"] *{
    color:white;
}

div[data-testid="metric-container"]{
    background:white;
    border-radius:12px;
    padding:20px;
    border:1px solid #E5E7EB;
    box-shadow:0px 4px 10px rgba(0,0,0,0.05);
}

</style>
""", unsafe_allow_html=True)



DATA_PATH = "data/analyzed_stock_data.csv"

if not os.path.exists(DATA_PATH):
    st.error("Run analysis.py first.")
    st.stop()

df = pd.read_csv(DATA_PATH)

df["Date"] = pd.to_datetime(df["Date"])

# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------

st.sidebar.title("📈 AI Stock Market Analyzer")

st.sidebar.markdown("---")

stock_list = sorted(df["Ticker"].unique())

selected_stock = st.sidebar.selectbox(
    "Select Company",
    stock_list
)

st.sidebar.markdown("---")

st.sidebar.info("""
### Project

AI Powered Real-Time
Stock Market Analyzer

**Developer**

Abithashri PS
""")

st.sidebar.markdown("---")

if st.sidebar.button("🔄 Refresh Dashboard"):
    st.rerun()

# -------------------------------------------------------
# TITLE
# -------------------------------------------------------

st.title("📈 AI Powered Real-Time Stock Market Analyzer")

st.caption("Live Market Dashboard using Python • Streamlit • Plotly • yFinance")

st.markdown("---")

# -------------------------------------------------------
# FILTER DATA
# -------------------------------------------------------

filtered_df = df[df["Ticker"] == selected_stock]

latest = (
    df.sort_values("Date")
      .groupby("Ticker")
      .tail(1)
)

# -------------------------------------------------------
# KPI VALUES
# -------------------------------------------------------

top_gainer = latest.loc[latest["Daily Return (%)"].idxmax()]

top_loser = latest.loc[latest["Daily Return (%)"].idxmin()]

avg_close = latest["Close"].mean()

total_volume = latest["Volume"].sum()

# -------------------------------------------------------
# KPI CARDS
# -------------------------------------------------------

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "🏆 Top Gainer",
        top_gainer["Ticker"],
        f"{top_gainer['Daily Return (%)']:.2f}%"
    )

with col2:
    st.metric(
        "📉 Top Loser",
        top_loser["Ticker"],
        f"{top_loser['Daily Return (%)']:.2f}%"
    )

with col3:
    st.metric(
        "💰 Avg Closing Price",
        f"${avg_close:.2f}"
    )

with col4:
    st.metric(
        "📦 Total Volume",
        f"{int(total_volume):,}"
    )

st.markdown("---")
# =====================================================
# CLOSING PRICE TREND
# =====================================================

st.subheader(f"📈 {selected_stock} Closing Price Trend")

fig_price = px.line(
    filtered_df,
    x="Date",
    y="Close",
    markers=True,
    title=f"{selected_stock} Closing Price"
)

fig_price.update_layout(
    template="plotly_white",
    height=450,
    xaxis_title="Date",
    yaxis_title="Closing Price ($)"
)

st.plotly_chart(fig_price, use_container_width=True)

st.markdown("---")

# =====================================================
# MOVING AVERAGE CHART
# =====================================================

st.subheader("📉 Moving Average Analysis")

fig_ma = go.Figure()

fig_ma.add_trace(
    go.Scatter(
        x=filtered_df["Date"],
        y=filtered_df["Close"],
        mode="lines",
        name="Close Price"
    )
)

fig_ma.add_trace(
    go.Scatter(
        x=filtered_df["Date"],
        y=filtered_df["MA5"],
        mode="lines",
        name="MA5"
    )
)

fig_ma.add_trace(
    go.Scatter(
        x=filtered_df["Date"],
        y=filtered_df["MA10"],
        mode="lines",
        name="MA10"
    )
)

fig_ma.update_layout(
    template="plotly_white",
    height=450,
    title="Moving Average (MA5 & MA10)",
    xaxis_title="Date",
    yaxis_title="Price ($)"
)

st.plotly_chart(fig_ma, use_container_width=True)

st.markdown("---")

# =====================================================
# TWO COLUMN LAYOUT
# =====================================================

col_left, col_right = st.columns(2)

# =====================================================
# DAILY RETURN
# =====================================================

with col_left:

    st.subheader("📊 Daily Return (%)")

    fig_return = px.bar(
        filtered_df,
        x="Date",
        y="Daily Return (%)",
        color="Daily Return (%)",
        text="Daily Return (%)"
    )

    fig_return.update_layout(
        template="plotly_white",
        height=420,
        showlegend=False
    )

    st.plotly_chart(fig_return, use_container_width=True)

# =====================================================
# TRADING VOLUME
# =====================================================

with col_right:

    st.subheader("📦 Trading Volume")

    fig_volume = px.bar(
        filtered_df,
        x="Date",
        y="Volume",
        text="Volume"
    )

    fig_volume.update_layout(
        template="plotly_white",
        height=420,
        showlegend=False
    )

    st.plotly_chart(fig_volume, use_container_width=True)

st.markdown("---")

# =====================================================
# PRICE STATISTICS
# =====================================================

st.subheader("📊 Price Statistics")

stat1, stat2, stat3, stat4 = st.columns(4)

with stat1:
    st.metric(
        "Highest Price",
        f"${filtered_df['High'].max():.2f}"
    )

with stat2:
    st.metric(
        "Lowest Price",
        f"${filtered_df['Low'].min():.2f}"
    )

with stat3:
    st.metric(
        "Average Close",
        f"${filtered_df['Close'].mean():.2f}"
    )

with stat4:
    st.metric(
        "Trading Days",
        filtered_df.shape[0]
    )

st.markdown("---")
# ==========================================================
# AI MARKET SUMMARY
# ==========================================================

st.subheader("🤖 AI Market Summary")

summary_file = "data/ai_summary.txt"

if os.path.exists(summary_file):

    with open(summary_file, "r") as file:
        summary = file.read()

    st.info(summary)

else:

    st.warning("AI Summary not found. Run ai_summary.py")

st.markdown("---")

# ==========================================================
# LIVE STOCK DATA
# ==========================================================

st.subheader("📋 Live Stock Data")

display_columns = [
    "Date",
    "Ticker",
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
    "Daily Return (%)",
    "MA5",
    "MA10"
]

st.dataframe(
    filtered_df[display_columns],
    use_container_width=True,
    height=450
)

st.markdown("---")

# ==========================================================
# DOWNLOAD BUTTON
# ==========================================================

st.subheader("📥 Download Data")

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download CSV",
    data=csv,
    file_name=f"{selected_stock}_stock_data.csv",
    mime="text/csv"
)

st.markdown("---")

# ==========================================================
# MARKET OVERVIEW
# ==========================================================

st.subheader("🌍 Market Overview")

overview = latest[[
    "Ticker",
    "Close",
    "Daily Return (%)",
    "Volume"
]].copy()

overview = overview.sort_values(
    by="Daily Return (%)",
    ascending=False
)

st.dataframe(
    overview,
    use_container_width=True,
    height=450
)

st.markdown("---")

# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
"""
---
### 👩‍💻 Project Information

**Project Name:** AI Powered Real-Time Stock Market Analyzer

**Developer:** Abithashri PS

**Technology Stack**

- Python
- Streamlit
- Plotly
- Pandas
- yFinance
- VS Code

**Features**

✅ Live Stock Data

✅ Daily Return Analysis

✅ Moving Average Analysis

✅ Interactive Charts

✅ AI Generated Market Summary

✅ Download CSV

✅ Professional Dashboard

---
"""
)