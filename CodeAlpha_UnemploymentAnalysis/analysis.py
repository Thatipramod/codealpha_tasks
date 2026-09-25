from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Project folders
BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "data" / "raw"
CLEAN_DIR = BASE_DIR / "data" / "cleaned"
OUTPUT_DIR = BASE_DIR / "outputs"

CLEAN_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid")


# Find the dataset
def find_csv_file():
    files = list(RAW_DIR.glob("*.csv"))

    if not files:
        raise FileNotFoundError(
            "No CSV file found in data/raw. Add the CodeAlpha dataset there."
        )

    return files[0]


# Clean column names
def clean_column_names(df):
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )
    return df


# Rename common dataset column names
def rename_columns(df):
    column_map = {}

    for column in df.columns:
        if column in ["region", "state", "states", "state_name"]:
            column_map[column] = "region"

        elif column in ["date", "month", "observation_date"]:
            column_map[column] = "date"

        elif column in [
            "estimated_unemployment_rate",
            "estimated_unemployment_rate_percent",
            "unemployment_rate",
            "unemployment_rate_percent",
        ]:
            column_map[column] = "unemployment_rate"

        elif column in ["estimated_employed", "employed", "employment"]:
            column_map[column] = "employed"

        elif column in [
            "estimated_labour_participation_rate",
            "estimated_labour_participation_rate_percent",
            "labour_participation_rate",
            "labor_participation_rate",
        ]:
            column_map[column] = "labour_participation_rate"

    return df.rename(columns=column_map)


# Load and clean the data
def load_data():
    file_path = find_csv_file()

    df = pd.read_csv(file_path)
    df = clean_column_names(df)
    df = rename_columns(df)

    if "date" not in df.columns:
        raise ValueError("Date column was not found in the dataset.")

    if "unemployment_rate" not in df.columns:
        raise ValueError("Unemployment rate column was not found.")

    # Convert dates and numeric columns
    df["date"] = pd.to_datetime(df["date"], errors="coerce", dayfirst=True)

    numeric_columns = [
        "unemployment_rate",
        "employed",
        "labour_participation_rate",
    ]

    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    # Remove unusable rows and duplicates
    df = df.dropna(subset=["date", "unemployment_rate"])
    df = df.drop_duplicates()

    if "region" in df.columns:
        df["region"] = df["region"].astype(str).str.strip()

    # Add useful columns for analysis
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["month_name"] = df["date"].dt.strftime("%B")

    # March 2020 onward is treated as the COVID-19 period
    df["covid_period"] = np.where(
        df["date"] >= pd.Timestamp("2020-03-01"),
        "COVID-19 Period",
        "Before COVID-19",
    )

    return df


# Show basic dataset information
def show_basic_information(df):
    print("\nDataset Overview")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("Date range:", df["date"].min().date(), "to", df["date"].max().date())

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate rows:", df.duplicated().sum())

    print("\nUnemployment rate statistics:")
    print(df["unemployment_rate"].describe())


# Save cleaned data
def save_cleaned_data(df):
    output_file = CLEAN_DIR / "unemployment_cleaned.csv"

    save_df = df.copy()
    save_df["date"] = save_df["date"].dt.strftime("%Y-%m-%d")
    save_df.to_csv(output_file, index=False)

    print(f"\nCleaned data saved to: {output_file}")


# Save charts
def save_chart(fig, filename):
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / filename, dpi=150, bbox_inches="tight")
    plt.close(fig)


# Overall unemployment trend
def overall_trend(df):
    trend = (
        df.groupby("date")["unemployment_rate"].mean().reset_index().sort_values("date")
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.lineplot(
        data=trend,
        x="date",
        y="unemployment_rate",
        marker="o",
        ax=ax,
    )

    ax.set_title("Overall Unemployment Rate Trend")
    ax.set_xlabel("Date")
    ax.set_ylabel("Average Unemployment Rate (%)")
    ax.tick_params(axis="x", rotation=45)

    save_chart(fig, "overall_unemployment_trend.png")


# Yearly unemployment analysis
def yearly_analysis(df):
    yearly = df.groupby("year")["unemployment_rate"].mean().reset_index()

    print("\nYearly Average Unemployment:")
    print(yearly.to_string(index=False))

    fig, ax = plt.subplots(figsize=(9, 5))

    sns.barplot(
        data=yearly,
        x="year",
        y="unemployment_rate",
        hue="year",
        legend=False,
        ax=ax,
    )

    ax.set_title("Average Unemployment Rate by Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Average Unemployment Rate (%)")

    save_chart(fig, "yearly_unemployment.png")


# Unemployment rate distribution
def unemployment_distribution(df):
    fig, ax = plt.subplots(figsize=(9, 5))

    sns.histplot(
        df["unemployment_rate"],
        kde=True,
        bins=20,
        ax=ax,
    )

    ax.set_title("Unemployment Rate Distribution")
    ax.set_xlabel("Unemployment Rate (%)")
    ax.set_ylabel("Frequency")

    save_chart(fig, "unemployment_distribution.png")


# Correlation between numeric variables
def correlation_analysis(df):
    numeric_data = df.select_dtypes(include=np.number)

    if numeric_data.shape[1] < 2:
        return

    correlation = numeric_data.corr()

    print("\nCorrelation Matrix:")
    print(correlation.round(2))

    fig, ax = plt.subplots(figsize=(9, 6))

    sns.heatmap(
        correlation,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        ax=ax,
    )

    ax.set_title("Correlation Matrix")

    save_chart(fig, "correlation_matrix.png")


# COVID-19 analysis
def covid_analysis(df):
    summary = df.groupby("covid_period")["unemployment_rate"].mean().reset_index()

    print("\nCOVID-19 Analysis:")
    print(summary.to_string(index=False))

    fig, ax = plt.subplots(figsize=(8, 5))

    sns.barplot(
        data=summary,
        x="covid_period",
        y="unemployment_rate",
        hue="covid_period",
        legend=False,
        ax=ax,
    )

    ax.set_title("Unemployment Before and During COVID-19")
    ax.set_xlabel("")
    ax.set_ylabel("Average Unemployment Rate (%)")

    save_chart(fig, "covid_impact.png")

    # Monthly trend during COVID-19
    covid_data = df[df["date"] >= pd.Timestamp("2020-03-01")]

    if covid_data.empty:
        return

    monthly = covid_data.groupby("date")["unemployment_rate"].mean().reset_index()

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.lineplot(
        data=monthly,
        x="date",
        y="unemployment_rate",
        marker="o",
        ax=ax,
    )

    ax.set_title("Unemployment Trend During COVID-19")
    ax.set_xlabel("Date")
    ax.set_ylabel("Average Unemployment Rate (%)")
    ax.tick_params(axis="x", rotation=45)

    save_chart(fig, "covid_monthly_trend.png")


# Monthly seasonal analysis
def seasonal_analysis(df):
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

    print("\nMonthly Average Unemployment:")
    print(monthly[["month_name", "unemployment_rate"]].to_string(index=False))

    available_months = [
        month for month in month_order if month in monthly["month_name"].values
    ]

    fig, ax = plt.subplots(figsize=(11, 5))

    sns.barplot(
        data=monthly,
        x="month_name",
        y="unemployment_rate",
        hue="month_name",
        order=available_months,
        legend=False,
        ax=ax,
    )

    ax.set_title("Average Unemployment Rate by Month")
    ax.set_xlabel("Month")
    ax.set_ylabel("Average Unemployment Rate (%)")
    ax.tick_params(axis="x", rotation=45)

    save_chart(fig, "monthly_seasonal_pattern.png")


# Regional analysis
def regional_analysis(df):
    if "region" not in df.columns:
        return

    regional = (
        df.groupby("region")["unemployment_rate"]
        .mean()
        .reset_index()
        .sort_values("unemployment_rate", ascending=False)
    )

    print("\nRegional Analysis:")
    print(regional.head(15).to_string(index=False))

    regional.to_csv(
        OUTPUT_DIR / "regional_summary.csv",
        index=False,
    )

    top_regions = regional.head(15).sort_values("unemployment_rate")

    fig, ax = plt.subplots(figsize=(10, 7))

    sns.barplot(
        data=top_regions,
        x="unemployment_rate",
        y="region",
        hue="region",
        legend=False,
        ax=ax,
    )

    ax.set_title("Regions by Average Unemployment Rate")
    ax.set_xlabel("Average Unemployment Rate (%)")
    ax.set_ylabel("Region")

    save_chart(fig, "regional_unemployment.png")


# Run the complete analysis
def main():
    print("CodeAlpha Task 2 - Unemployment Analysis")

    df = load_data()

    show_basic_information(df)
    save_cleaned_data(df)

    overall_trend(df)
    yearly_analysis(df)
    unemployment_distribution(df)
    correlation_analysis(df)

    covid_analysis(df)
    seasonal_analysis(df)
    regional_analysis(df)

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()
