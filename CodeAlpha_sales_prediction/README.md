# 📊 Sales Prediction System

A Machine Learning based **Sales Prediction System** built using **Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn and Streamlit**.

The system predicts sales based on advertising expenditure across **TV, Radio and Newspaper** channels. It also provides model comparison, prediction analysis and feature-importance insights.

## 🚀 Live Demo

👉 **Streamlit App:** [Open Live Demo](https://sales-prediction-analytics.streamlit.app/)

---

## 📌 Project Overview

The objective of this project is to analyze the relationship between advertising expenditure and sales and build a machine learning model for sales prediction.

The project includes:

- 📊 Sales prediction
- 📺 TV advertising analysis
- 📻 Radio advertising analysis
- 📰 Newspaper advertising analysis
- 🔍 Data preprocessing
- 🤖 Multiple regression models
- 📋 Model performance comparison
- 🎯 Actual vs Predicted analysis
- 📉 Prediction error analysis
- ⭐ Feature importance analysis
- 🌐 Interactive Streamlit dashboard

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Streamlit | Web application |
| Joblib | Model saving and loading |
| Git & GitHub | Version control |

---

## 📂 Dataset

The project uses the **Advertising.csv** dataset.

### Features

| Feature | Description |
|---|---|
| `TV` | TV advertising expenditure |
| `Radio` | Radio advertising expenditure |
| `Newspaper` | Newspaper advertising expenditure |
| `Sales` | Target variable |

The unnecessary `Unnamed: 0` index column is removed during preprocessing.

---

## 🔄 Machine Learning Workflow

```text
Advertising Dataset
        ↓
Data Loading
        ↓
Data Cleaning
        ↓
Missing Value & Duplicate Check
        ↓
Exploratory Data Analysis
        ↓
Feature Selection
        ↓
Train/Test Split
        ↓
Regression Models
        ↓
Model Evaluation
        ↓
Best Model Selection
        ↓
Sales Prediction
        ↓
Streamlit Application
        ↓
Deployment
```

---

## 🤖 Machine Learning Models

Three regression algorithms are compared:

### 1. Linear Regression

Used to model the linear relationship between advertising expenditure and sales.

### 2. Decision Tree Regressor

Uses decision-based rules to predict sales from advertising features.

### 3. Random Forest Regressor

An ensemble model that combines multiple decision trees to improve prediction performance.

---

## 📏 Model Evaluation

The models are evaluated using the following metrics:

| Metric | Description |
|---|---|
| **MAE** | Mean Absolute Error |
| **RMSE** | Root Mean Squared Error |
| **R² Score** | Coefficient of Determination |

The best-performing model is selected based on the evaluation results obtained from the test dataset.

---

## 🖥️ Streamlit Application

The project includes an interactive Streamlit dashboard with the following sections:

- 🏠 **Home / Dashboard**
- 🔮 **Sales Prediction**
- 📊 **Data Insights**
- 🤖 **Model Performance**
- ⭐ **Feature Importance**
- ℹ️ **About**

Users can enter advertising expenditure values and receive a predicted sales value through the application.

---

## 📊 Analysis & Insights

The application helps analyze:

- The relationship between advertising expenditure and sales.
- The performance of different regression models.
- The importance of individual advertising features.
- The difference between actual and predicted sales.
- Prediction errors produced by the selected model.

---

## 📁 Project Structure

```text
CodeAlpha_SalesPrediction/
│
├── CodeAlpha_sales_prediction/
│   │
│   ├── Images/
│   │   ├── actual_vs_predicted.png
│   │   ├── correlation_matrix.png
│   │   ├── feature_importance.png
│   │   ├── newspaper_vs_sales.png
│   │   ├── prediction_error_analysis.png
│   │   ├── radio_vs_sales.png
│   │   ├── sales_distribution.png
│   │   ├── total_advertising_vs_sales.png
│   │   └── tv_vs_sales.png
│   │
│   ├── models/
│   │   └── sales_prediction_model.pkl
│   │
│   ├── pages/
│   │
│   ├── app.py
│   ├── model_utils.py
│   ├── cleaned_data.csv
│   ├── Advertising.csv
│   └── requirements.txt
│
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

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

### Live Application

👉 [Sales Prediction Streamlit App](https://sales-prediction-analytics.streamlit.app/)

---

## 🔗 Project Links

### GitHub Repository

👉 [GitHub Repository](https://github.com/Thatipramod/codealpha_tasks/tree/main)

### Live Streamlit App

👉 [Streamlit Live Demo](https://sales-prediction-analytics.streamlit.app/)

### LinkedIn

👉 [LinkedIn Profile](https://www.linkedin.com/in/thati-pramod/)

---

## 🎓 CodeAlpha Internship

This project was developed as part of the **CodeAlpha Data Science Internship — Task 4: Sales Prediction using Python**.

### Skills Demonstrated

- Data preprocessing
- Exploratory Data Analysis
- Data visualization
- Feature selection
- Regression modelling
- Model evaluation
- Sales prediction
- Streamlit application development
- Machine learning deployment

---

## 👨‍💻 Developed By

**Thati Pramod**

B.Tech — Computer Science & Engineering (AI & ML)

---

## 📜 License

This project is intended for **educational and internship purposes**.
