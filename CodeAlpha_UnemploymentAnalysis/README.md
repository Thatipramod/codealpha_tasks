# 📊 Unemployment Analysis with Python

A Data Analysis and Visualization project built using **Python, Pandas, NumPy, Matplotlib, Seaborn and Streamlit**.

The project analyzes unemployment rate data, identifies **unemployment trends, seasonal patterns, regional variations and the impact of COVID-19**, and presents the results through an interactive Streamlit dashboard.

---

## 🚀 Live Demo

👉 **Streamlit App:https://unemployment-analytics.streamlit.app/

---

## 📌 Project Overview

The objective of this project is to analyze unemployment rate data and understand how unemployment changed over time, across regions and during the COVID-19 period.

The project includes:

- 📊 Unemployment rate analysis
- 📈 Overall unemployment trends
- 📅 Year-wise analysis
- 🦠 COVID-19 impact analysis
- 📆 Monthly and seasonal patterns
- 🗺️ Regional unemployment analysis
- 🔍 Data cleaning and preprocessing
- 📉 Unemployment rate distribution
- 📋 Summary tables
- 💡 Key analytical insights
- 🌐 Interactive Streamlit dashboard

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Pandas | Data cleaning and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Streamlit | Interactive dashboard |
| Git & GitHub | Version control |

---

## 📂 Dataset

The project uses unemployment rate data representing the percentage of unemployed people.

The dataset contains information such as:

| Feature | Description |
|---|---|
| `date` | Observation date |
| `region` | State/region information |
| `unemployment_rate` | Unemployment rate (%) |
| `employed` | Estimated number of employed people |
| `labour_participation_rate` | Labour participation rate |
| `year` | Year extracted from the date |
| `month` | Month number |
| `month_name` | Month name |
| `covid_period` | COVID-19 period classification |

The raw dataset is cleaned and transformed before being used by the Streamlit application.

---

## 🔄 Data Analysis Workflow

```text
Raw Unemployment Dataset
        ↓
Data Loading
        ↓
Column Cleaning & Standardization
        ↓
Date & Numeric Conversion
        ↓
Missing Value Handling
        ↓
Duplicate Removal
        ↓
Feature Preparation
        ↓
Exploratory Data Analysis
        ↓
Unemployment Trend Analysis
        ↓
COVID-19 Impact Analysis
        ↓
Seasonal / Monthly Analysis
        ↓
Regional Analysis
        ↓
Charts & Insights
        ↓
Streamlit Dashboard
        ↓
Deployment
```

---

## 📊 Analysis Performed

### 1. Overall Unemployment Trend

Analyzes how the unemployment rate changed over time and helps identify major increases and decreases in unemployment.

### 2. Yearly Analysis

Calculates the average unemployment rate for each year to compare unemployment levels across different years.

### 3. Unemployment Distribution

Visualizes the distribution of unemployment rates using a histogram and density analysis.

### 4. COVID-19 Impact

Compares unemployment levels before and during the COVID-19 period.

For this project, observations from **March 2020 onward** are categorized under the COVID-19 timeframe.

### 5. Monthly / Seasonal Analysis

Analyzes the average unemployment rate for each month to identify recurring monthly patterns.

### 6. Regional Analysis

Compares average unemployment rates across regions and identifies regions with higher average unemployment rates.

---

## 📈 Visualizations

The project generates the following visualizations:

- Overall unemployment trend
- Yearly unemployment analysis
- Unemployment rate distribution
- COVID-19 impact
- COVID-19 monthly trend
- Monthly seasonal pattern
- Regional unemployment analysis
- Correlation matrix

---

## 🖥️ Streamlit Application

The project includes an interactive Streamlit dashboard with the following sections:

- 📊 **Overview**
- 🦠 **COVID-19 Impact**
- 📅 **Seasonal Trends**
- 🗺️ **Regional Analysis**
- 📑 **Raw Data**

### Dashboard Features

- Date range filtering
- Region filtering
- KPI cards
- Interactive data tables
- Unemployment trend visualization
- COVID-19 comparison
- Monthly analysis
- Regional analysis
- Filtered CSV export
- Key analytical takeaways

---

## 📊 Dashboard KPIs

The dashboard displays:

| KPI | Description |
|---|---|
| **Total Records** | Number of records after applying filters |
| **Average Rate** | Average unemployment rate |
| **Peak Rate** | Highest unemployment rate |
| **Lowest Rate** | Lowest unemployment rate |

---

## 📁 Project Structure

```text
CodeAlpha_UnemploymentAnalysis/
│
├── data/
│   ├── raw/
│   │   └── Unemployment in India.csv
│   │
│   └── cleaned/
│       └── unemployment_cleaned.csv
│
├── outputs/
│   ├── correlation_matrix.png
│   ├── covid_impact.png
│   ├── covid_monthly_trend.png
│   ├── monthly_seasonal_pattern.png
│   ├── overall_unemployment_trend.png
│   ├── regional_summary.csv
│   ├── regional_unemployment.png
│   ├── unemployment_distribution.png
│   └── yearly_unemployment.png
│
├── analysis.py
├── app.py
├── style.css
├── requirements.txt
└── README.md
```

---

## ▶️ Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Thatipramod/codealpha_tasks.git
```

### 2. Open the Project

```bash
cd codealpha_tasks
```

If the project is inside a separate folder:

```bash
cd CodeAlpha_UnemploymentAnalysis
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Analysis

First run the data analysis and cleaning script:

```bash
python analysis.py
```

This generates the cleaned dataset and analysis visualizations.

### 5. Run the Streamlit Application

```bash
streamlit run app.py
```

The dashboard will open in your browser.

---

## 📦 Requirements

The project uses:

```text
pandas
numpy
matplotlib
seaborn
streamlit
```

All dependencies are listed in `requirements.txt`.

---

## 🌐 Deployment

The Streamlit dashboard can be deployed using **Streamlit Community Cloud**.

### Deployment Files

Make sure the repository contains:

```text
app.py
style.css
requirements.txt
data/cleaned/unemployment_cleaned.csv
```

Then select `app.py` as the main application file during deployment.

---

## 🔗 Project Links

### GitHub Repository

👉 [GitHub Repository](https://github.com/Thatipramod/codealpha_tasks)

### Live Streamlit App

👉 *Add your Streamlit deployment link here*

### LinkedIn

👉 [LinkedIn Profile](https://www.linkedin.com/in/thati-pramod/)

---

## 🎓 CodeAlpha Internship

This project was developed as part of the **CodeAlpha Data Science Internship — Task 2: Unemployment Analysis with Python**.

The task focuses on unemployment data cleaning, exploration and visualization, including analysis of unemployment trends, COVID-19 impact and seasonal patterns.

---

## 💡 Key Skills Demonstrated

- Data cleaning
- Data preprocessing
- Exploratory Data Analysis
- Data visualization
- Time-series analysis
- COVID-19 impact analysis
- Seasonal pattern analysis
- Regional analysis
- Pandas data manipulation
- Matplotlib visualization
- Seaborn visualization
- Streamlit dashboard development
- Git & GitHub
- Data analysis project deployment

---

## 👨‍💻 Developed By

**Thati Pramod**

B.Tech — Computer Science & Engineering (AI & ML)

**Data Science & Machine Learning Enthusiast**

---

## 📜 License

This project is intended for **educational and internship purposes**.
