# 📊 Sales Prediction System

A Machine Learning based **Sales Prediction System** built using **Python, Pandas, Scikit-learn, Matplotlib, Seaborn and Streamlit**.

The application predicts product sales using advertising expenditure across **TV, Radio and Newspaper** channels. It also provides interactive data analysis, model comparison and feature-importance insights.

## 🚀 Live Demo

👉 **Streamlit App:** [Open Live Demo](https://sales-prediction-analytics.streamlit.app/)

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
- 🌐 Interactive Streamlit dashboard

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Pandas | Data handling |
| NumPy | Numerical operations |
| Matplotlib | Visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine Learning |
| Streamlit | Web application |
| Joblib | Model saving/loading |
| Git & GitHub | Version control |

## 📂 Dataset

The project uses an `Advertising.csv` dataset containing advertising expenditure and sales information.

### Features

- `TV` — TV advertising expenditure
- `Radio` — Radio advertising expenditure
- `Newspaper` — Newspaper advertising expenditure
- `Sales` — Target variable

The unnecessary `Unnamed: 0` index column is removed during preprocessing.

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
```

## 🤖 Models Used

The project compares multiple regression models:

1. **Linear Regression**
2. **Decision Tree Regressor**
3. **Random Forest Regressor**

### Evaluation Metrics

- **MAE** — Mean Absolute Error
- **RMSE** — Root Mean Squared Error
- **R² Score** — Coefficient of Determination

The final model is selected based on the evaluation results obtained on the test dataset.

## 🖥️ Application Screenshots

### 🏠 Home / Dashboard

Add your Home or Dashboard screenshot here:

```text
images/dashboard.png
```

```markdown
![Dashboard](images/dashboard.png)
```

### 🔮 Predict Sales

Add the Predict Sales page screenshot:

```text
images/predict_sales.png
```

```markdown
![Predict Sales](images/predict_sales.png)
```

### 📊 Data Insights

Add the Data Insights page screenshot:

```text
images/data_insights.png
```

```markdown
![Data Insights](images/data_insights.png)
```

### 🤖 Model Performance

Add the Model Performance page screenshot:

```text
images/model_performance.png
```

```markdown
![Model Performance](images/model_performance.png)
```

### 📈 Feature Importance

Add the Feature Importance page screenshot:

```text
images/feature_importance.png
```

```markdown
![Feature Importance](images/feature_importance.png)
```

### ℹ️ About

![About](images/about.png)

## 📸 Screenshot Checklist

Before pushing the final project to GitHub, save screenshots with these exact names:

```text
images/
├── dashboard.png
├── predict_sales.png
├── data_insights.png
├── model_performance.png
├── feature_importance.png
└── about.png
```

The README is already prepared for these images. Just place the remaining screenshots in the `images` folder.

## 📊 Key Business Insights

The application helps analyze:

- Which advertising channel has a stronger relationship with sales.
- How advertising expenditure changes predicted sales.
- How different regression models perform.
- Which features are most important to the selected model.
- How close predicted sales are to actual sales.

> Update this section with the exact findings from your final model and analysis. Do not claim specific percentages unless they come from your actual results.

## 📁 Project Structure

```text
CodeAlpha_SalesPrediction/
│
├── data/
│   └── Advertising.csv
│
├── notebooks/
│   └── Sales_Prediction.ipynb
│
├── models/
│   └── sales_prediction_model.pkl
│
├── app/
│   └── app.py
│
├── images/
│   ├── dashboard.png
│   ├── predict_sales.png
│   ├── data_insights.png
│   ├── model_performance.png
│   ├── feature_importance.png
│   └── about.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPO_URL
cd CodeAlpha_SalesPrediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run app/app.py
```

The application will open in your browser.

## 🌐 Deployment

The application can be deployed using **Streamlit Community Cloud** from the GitHub repository.

After deployment, add the live URL at the top of this README under **Live Demo**.

## 🔗 Project Links

### GitHub Repository

👉 [GitHub Repository](YOUR_GITHUB_REPO_URL)

### Live Streamlit App

👉 [Streamlit Live Demo](YOUR_STREAMLIT_APP_URL)

### LinkedIn

👉 [LinkedIn Profile](YOUR_LINKEDIN_PROFILE_URL)

👉 [LinkedIn Project Post](YOUR_LINKEDIN_POST_URL)

> Replace all placeholder URLs with your actual links before submitting the project.

## 🎓 CodeAlpha Internship

This project was developed as part of the **CodeAlpha Data Science Internship — Task 4: Sales Prediction using Python**.

The task focuses on data preparation, feature selection, regression/time-series based sales prediction, advertising impact analysis and actionable business insights.

## 👨‍💻 Developed By

**Thati Pramod**

B.Tech — Computer Science & Engineering (AI & ML)

## 📜 License

This project is intended for educational and internship purposes.
