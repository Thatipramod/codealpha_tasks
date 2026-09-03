import os

import streamlit as st

from model_utils import load_data, train_models

# Page Configuration
st.set_page_config(
    page_title="Sales Prediction System",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Load Custom CSS
def load_css(css_file="style.css"):
    if os.path.exists(css_file):
        with open(css_file, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css()


# Load Cleaned Data
@st.cache_data
def get_data():
    return load_data("cleaned_data.csv")


# Train Models
@st.cache_resource
def get_models(df):
    return train_models(df)


df = get_data()
best_model, best_model_name, model_results, y_test, predictions = get_models(df)


# Home Page
def show_home():
    st.title("📈 Sales Prediction System")
    st.write(
        "Predict product sales using TV, Radio, and Newspaper advertising budgets."
    )

    st.success("✅ Machine Learning Model Loaded Successfully")
    st.divider()

    # Project Metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Best Model", best_model_name)

    with col2:
        st.metric("Total Records", len(df))

    with col3:
        st.metric("Advertising Channels", "3")

    with col4:
        st.metric("Average Sales", f"{df['Sales'].mean():.2f}k")

    st.divider()

    # Project Overview
    st.subheader("💡 Project Overview")
    st.write(
        """
        This application uses Machine Learning to predict product sales
        based on advertising expenditure.

        The project compares three regression models:
        • Linear Regression
        • Decision Tree
        • Random Forest

        Model performance is evaluated using MAE, RMSE, and R² Score.
        The model with the highest R² Score is selected as the primary model.
        """
    )

    st.divider()

    # Key Features
    st.subheader("🚀 Key Features")

    col1, col2 = st.columns(2)

    with col1:
        st.write("📺 TV Advertising Analysis")
        st.write("📻 Radio Advertising Analysis")
        st.write("📰 Newspaper Advertising Analysis")
        st.write("🔮 Sales Prediction")

    with col2:
        st.write("📊 Data Insights")
        st.write("🤖 Model Performance")
        st.write("📈 Feature Importance")
        st.write("ℹ️ Project Information")

    st.info("👈 Use the navigation menu on the left sidebar to explore the project.")

    st.divider()

    # Footer
    st.markdown(
        "<div style='text-align:center;color:#888;font-size:0.9rem;'>"
        "Made with ❤️ by <b>Thati Pramod</b>"
        "</div>",
        unsafe_allow_html=True,
    )


# Navigation Pages
home_page = st.Page(show_home, title="Home", icon="🏠", default=True)

predict_sales = st.Page("pages/predict_sales.py", title="Predict Sales", icon="🔮")

data_insights = st.Page("pages/Data_Insights.py", title="Data Insights", icon="📊")

model_performance = st.Page(
    "pages/Model_Performance.py", title="Model Performance", icon="🤖"
)

feature_importance = st.Page(
    "pages/Feature_Importance.py", title="Feature Importance", icon="📈"
)

about = st.Page("pages/About.py", title="About", icon="ℹ️")


# Sidebar Navigation
pg = st.navigation(
    {
        "Main App": [home_page, predict_sales],
        "Analytics & ML": [data_insights, model_performance, feature_importance],
        "Information": [about],
    }
)


# Sidebar Footer
with st.sidebar:
    st.divider()
    st.markdown("👨‍💻 **Developed by:**")
    st.markdown("### **Thati Pramod**")
    st.caption("© 2026 Sales Prediction System")


# Run Selected Page
pg.run()
