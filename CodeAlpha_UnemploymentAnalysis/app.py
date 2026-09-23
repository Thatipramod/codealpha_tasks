from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

# Configuration
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "cleaned" / "unemployment_cleaned.csv"
STYLE_FILE = BASE_DIR / "style.css"

st.set_page_config(
    page_title="Unemployment Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Load dashboard CSS
def load_css():
    if STYLE_FILE.exists():
        st.markdown(f"<style>{STYLE_FILE.read_text()}</style>", unsafe_allow_html=True)


load_css()


# Theme colors
BG_COLOR = "#F3F4F3"
CARD_COLOR = "#FFFFFF"
TEXT_COLOR = "#252A2A"
MUTED_COLOR = "#6B7280"
ACCENT_COLOR = "#A45A3F"
BORDER_COLOR = "#D1D5D5"
plt.rcParams.update(
    {
        "figure.facecolor": CARD_COLOR,
        "axes.facecolor": CARD_COLOR,
        "savefig.facecolor": CARD_COLOR,
        "text.color": TEXT_COLOR,
        "axes.labelcolor": TEXT_COLOR,
        "xtick.color": TEXT_COLOR,
        "ytick.color": TEXT_COLOR,
        "grid.color": GRID_COLOR,
        "grid.linestyle": "--",
        "grid.alpha": 0.6,
        "font.family": "sans-serif",
    }
)


# Load cleaned data
@st.cache_data
def load_data():
    if not DATA_FILE.exists():
        return None

    df = pd.read_csv(DATA_FILE)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    return df.dropna(subset=["date", "unemployment_rate"])


# Overall trend
def build_trend_chart(df):
    trend = (
        df.groupby("date")["unemployment_rate"].mean().reset_index().sort_values("date")
    )

    fig, ax = plt.subplots(figsize=(10, 4.2))
    ax.grid(True, axis="y")
    ax.plot(
        trend["date"], trend["unemployment_rate"], color=ACCENT_COLOR, linewidth=2.5
    )
    ax.fill_between(
        trend["date"], trend["unemployment_rate"], color=ACCENT_COLOR, alpha=0.12
    )
    ax.set_title("Unemployment Rate Timeline", fontsize=12, pad=12, fontweight="bold")
    ax.set_ylabel("Rate (%)")
    ax.tick_params(axis="x", rotation=30)
    sns.despine(top=True, right=True)
    fig.tight_layout()
    return fig


# Yearly average
def build_yearly_chart(df):
    yearly = df.groupby("year")["unemployment_rate"].mean().reset_index()

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.grid(True, axis="y")

    sns.barplot(
        data=yearly,
        x="year",
        y="unemployment_rate",
        hue="year",
        palette="Oranges",
        legend=False,
        ax=ax,
    )

    ax.set_title("Annual Average Rate", fontsize=11, fontweight="bold")
    ax.set_xlabel("")
    ax.set_ylabel("Rate (%)")
    sns.despine(top=True, right=True)
    fig.tight_layout()
    return fig


# Rate distribution
def build_distribution_chart(df):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.grid(True, axis="y")

    sns.histplot(
        df["unemployment_rate"],
        kde=True,
        color="#D97706",
        bins=20,
        edgecolor=CARD_COLOR,
        ax=ax,
    )

    ax.set_title("Rate Distribution", fontsize=11, fontweight="bold")
    ax.set_xlabel("Unemployment Rate (%)")
    ax.set_ylabel("Frequency")
    sns.despine(top=True, right=True)
    fig.tight_layout()
    return fig


# COVID-19 comparison
def build_covid_chart(df):
    if "covid_period" not in df.columns:
        return None

    summary = df.groupby("covid_period")["unemployment_rate"].mean().reset_index()

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.grid(True, axis="y")

    sns.barplot(
        data=summary,
        x="covid_period",
        y="unemployment_rate",
        hue="covid_period",
        palette=["#78716C", "#C2410C"],
        legend=False,
        ax=ax,
    )

    ax.set_title("Pre vs COVID-19 Period", fontsize=11, fontweight="bold")
    ax.set_xlabel("")
    ax.set_ylabel("Average Rate (%)")
    sns.despine(top=True, right=True)
    fig.tight_layout()
    return fig


# Monthly pattern
def build_monthly_chart(df):
    month_order = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    monthly = (
        df.groupby(["month", "month_name"])["unemployment_rate"]
        .mean()
        .reset_index()
        .sort_values("month")
    )

    available = [
        month for month in month_order if month in monthly["month_name"].values
    ]

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.grid(True, axis="y")

    sns.barplot(
        data=monthly,
        x="month_name",
        y="unemployment_rate",
        hue="month_name",
        order=available,
        palette="YlOrBr",
        legend=False,
        ax=ax,
    )

    ax.set_title("Seasonal / Monthly Pattern", fontsize=11, fontweight="bold")
    ax.set_xlabel("")
    ax.set_ylabel("Average Rate (%)")
    ax.tick_params(axis="x", rotation=40)
    sns.despine(top=True, right=True)
    fig.tight_layout()
    return fig


# Regional analysis
def build_regional_chart(df):
    if "region" not in df.columns:
        return None

    regional = (
        df.groupby("region")["unemployment_rate"]
        .mean()
        .reset_index()
        .sort_values("unemployment_rate", ascending=False)
        .head(10)
    )

    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.grid(True, axis="x")

    sns.barplot(
        data=regional,
        x="unemployment_rate",
        y="region",
        hue="region",
        palette="rocket",
        legend=False,
        ax=ax,
    )

    ax.set_title("Top 10 High-Unemployment Regions", fontsize=11, fontweight="bold")
    ax.set_xlabel("Average Rate (%)")
    ax.set_ylabel("")
    sns.despine(top=True, right=True)
    fig.tight_layout()
    return fig


# Load data
df = load_data()

if df is None:
    st.error("Cleaned data file not found at `data/cleaned/unemployment_cleaned.csv`")
    st.info("Run your data cleaning script first.")
    st.stop()


# Sidebar branding
st.sidebar.markdown(
    '<div class="side-brand">'
    '<div class="side-icon">📊</div>'
    '<div><div class="side-title">Unemployment</div>'
    '<div class="side-subtitle">Analytics Dashboard</div></div>'
    "</div>",
    unsafe_allow_html=True,
)

st.sidebar.markdown("<div class='side-line'></div>", unsafe_allow_html=True)

st.sidebar.markdown("<div class='filter-title'>🎛️ Filters</div>", unsafe_allow_html=True)

st.sidebar.caption("Customize the dashboard view using the options below.")

min_date = df["date"].min().date()
max_date = df["date"].max().date()

date_range = st.sidebar.date_input(
    "Date Range", value=(min_date, max_date), min_value=min_date, max_value=max_date
)

if len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date = end_date = min_date

selected_region = "All Regions"

if "region" in df.columns:
    region_options = ["All Regions"] + sorted(df["region"].dropna().unique().tolist())
    selected_region = st.sidebar.selectbox("Region", region_options)


# Project information
st.sidebar.markdown(
    "<div class='side-space'></div>"
    "<div class='project-card'>"
    "<div class='project-heading'>📌 Project</div>"
    "<div class='project-name'>Unemployment Analysis</div>"
    "<div class='project-text'>"
    "Analysis of unemployment trends, COVID-19 impact, "
    "seasonal patterns and regional variations."
    "</div></div>",
    unsafe_allow_html=True,
)

# Developer information
st.sidebar.markdown(
    "<div class='side-space'></div>"
    "<div class='developer-card'>"
    "<div class='developer-label'>DEVELOPED BY</div>"
    "<div class='developer-name'>Pramod</div>"
    "<div class='developer-role'>B.Tech CSE (AI & ML)</div>"
    "<div class='developer-role'>Data Science & Analytics</div>"
    "<div class='developer-line'></div>"
    "<div class='developer-footer'>"
    "CodeAlpha Data Science Internship"
    "</div></div>",
    unsafe_allow_html=True,
)


# Apply filters
filtered_df = df[
    (df["date"].dt.date >= start_date) & (df["date"].dt.date <= end_date)
].copy()

if "region" in filtered_df.columns and selected_region != "All Regions":
    filtered_df = filtered_df[filtered_df["region"] == selected_region]

# Header
header = (
    '<div class="dashboard-header">'
    '<div class="main-title">Unemployment Analytics</div>'
    '<div class="sub-title">'
    "Labor trends, COVID-19 impact, seasonal patterns and regional analysis"
    "</div></div>"
)

st.markdown(header, unsafe_allow_html=True)

if filtered_df.empty:
    st.warning("No records match the selected filters.")
    st.stop()


# KPI cards
kpis = [
    ("Total Records", f"{len(filtered_df):,}"),
    ("Average Rate", f"{filtered_df['unemployment_rate'].mean():.2f}%"),
    ("Peak Rate", f"{filtered_df['unemployment_rate'].max():.2f}%"),
    ("Lowest Rate", f"{filtered_df['unemployment_rate'].min():.2f}%"),
]

for col, (label, value) in zip(st.columns(4), kpis):
    card = (
        '<div class="kpi-card">'
        f'<div class="kpi-label">{label}</div>'
        f'<div class="kpi-value">{value}</div>'
        "</div>"
    )
    with col:
        st.markdown(card, unsafe_allow_html=True)

st.write("")


# Dashboard tabs
tabs = st.tabs(
    [
        "📊 Overview",
        "🦠 COVID-19 Impact",
        "📅 Seasonal Trends",
        "🗺️ Regional Analysis",
        "📑 Raw Data",
    ]
)

# Overview
with tabs[0]:
    st.pyplot(build_trend_chart(filtered_df), use_container_width=True)

    left, right = st.columns(2)

    with left:
        st.pyplot(build_yearly_chart(filtered_df), use_container_width=True)

    with right:
        st.pyplot(build_distribution_chart(filtered_df), use_container_width=True)


# COVID-19 analysis
with tabs[1]:
    chart = build_covid_chart(filtered_df)

    if chart is not None:
        st.pyplot(chart, use_container_width=True)

    if "covid_period" in filtered_df.columns:
        summary = (
            filtered_df.groupby("covid_period")["unemployment_rate"]
            .mean()
            .reset_index()
            .rename(
                columns={
                    "covid_period": "Period",
                    "unemployment_rate": "Mean Unemployment Rate (%)",
                }
            )
        )

        st.dataframe(summary, use_container_width=True, hide_index=True)

        st.caption(
            "ℹ️ Data from March 2020 onward is categorized under the COVID-19 timeframe."
        )


# Seasonal trends
with tabs[2]:
    st.pyplot(build_monthly_chart(filtered_df), use_container_width=True)

    monthly = (
        filtered_df.groupby(["month", "month_name"])["unemployment_rate"]
        .mean()
        .reset_index()
        .sort_values("month")[["month_name", "unemployment_rate"]]
        .rename(
            columns={"month_name": "Month", "unemployment_rate": "Average Rate (%)"}
        )
    )

    st.dataframe(monthly, use_container_width=True, hide_index=True)


# Regional analysis
with tabs[3]:
    chart = build_regional_chart(filtered_df)

    if chart is None:
        st.warning("Regional data is missing from the dataset.")
    else:
        st.pyplot(chart, use_container_width=True)

        regional = (
            filtered_df.groupby("region")["unemployment_rate"]
            .agg(Average="mean", Minimum="min", Maximum="max", Records="count")
            .reset_index()
            .sort_values("Average", ascending=False)
        )

        st.dataframe(regional, use_container_width=True, hide_index=True)


# Raw data
with tabs[4]:
    st.markdown(f"**Dataset View** ({len(filtered_df):,} records)")

    st.dataframe(filtered_df, use_container_width=True, hide_index=True)

    csv_bytes = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Export Filtered CSV",
        data=csv_bytes,
        file_name="filtered_unemployment_data.csv",
        mime="text/csv",
    )


# Key insights
st.markdown("---")
st.subheader("💡 Key Takeaways")

yearly_means = filtered_df.groupby("year")["unemployment_rate"].mean()

if not yearly_means.empty:
    st.markdown(f"- **Peak Year:** {yearly_means.idxmax()} ({yearly_means.max():.2f}%)")

    st.markdown(
        f"- **Lowest Year:** {yearly_means.idxmin()} ({yearly_means.min():.2f}%)"
    )

if "region" in filtered_df.columns:
    region_means = filtered_df.groupby("region")["unemployment_rate"].mean()

    if not region_means.empty:
        st.markdown(
            f"- **Highest Average Region:** "
            f"{region_means.idxmax()} "
            f"({region_means.max():.2f}%)"
        )


# Footer
st.caption("Developed by Pramod | Unemployment Analysis with Python")
