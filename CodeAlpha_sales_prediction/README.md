# 📊 Sales Prediction System

A Machine Learning based **Sales Prediction System** built using **Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn and Streamlit**.

The application predicts product sales using advertising expenditure across **TV, Radio and Newspaper** channels. It also provides interactive data analysis, model comparison, prediction analysis and feature-importance insights.

## 🚀 Live Demo

👉 **Streamlit App:** [Open Live Demo](https://sales-prediction-analytics.streamlit.app/)

---

## 📌 Project Overview

The goal of this project is to understand how advertising expenditure affects sales and to build a regression-based machine learning system that can estimate sales from advertising budgets.

### Main Features

- 📊 Sales prediction
- 📺 TV advertising analysis
- 📻 Radio advertising analysis
- 📰 Newspaper advertising analysis
- 📈 Exploratory Data Analysis
- 🔗 Correlation analysis
- 🤖 Multiple regression models
- 📋 Model performance comparison
- 🎯 Actual vs Predicted analysis
- 📈 Feature importance analysis
- 📉 Prediction error analysis
- 🌐 Interactive Streamlit dashboard

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Pandas | Data handling and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine Learning |
| Streamlit | Web application |
| Joblib | Model saving and loading |
| Git & GitHub | Version control |

---

## 📂 Dataset

The project uses an `Advertising.csv` dataset containing advertising expenditure and sales information.

### Features

- `TV` — TV advertising expenditure
- `Radio` — Radio advertising expenditure
- `Newspaper` — Newspaper advertising expenditure
- `Sales` — Target variable

The unnecessary `Unnamed: 0` index column is removed during preprocessing.

---

## 🔄 Machine Learning Workflow

```text
Advertising Dataset
        ↓
Data Cleaning
        ↓
Duplicate & Missing Value Check
        ↓
Exploratory Data Analysis
        ↓
Correlation Analysis
        ↓
Feature Selection
        ↓
Train/Test Split
        ↓
Multiple Regression Models
        ↓
Model Evaluation
        ↓
Best Model Selection
        ↓
Sales Prediction
        ↓
Streamlit Deployment
