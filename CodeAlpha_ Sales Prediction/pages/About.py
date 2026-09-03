import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ️", layout="wide")

st.title("ℹ️ About This Project")

st.markdown("""
## 📈 Sales Prediction System

The **Sales Prediction System** is a Machine Learning application developed
using **Python** and **Streamlit**. It predicts product sales based on
advertising expenditure across **TV, Radio, and Newspaper** channels.

The application provides an easy-to-use interface for sales prediction,
data analysis, model comparison, and feature importance.
""")

st.markdown("---")
st.header("🚀 Features")
st.write("1️⃣ Sales Prediction")
st.write("2️⃣ TV Advertising Analysis")
st.write("3️⃣ Radio Advertising Analysis")
st.write("4️⃣ Newspaper Advertising Analysis")
st.write("5️⃣ Correlation Analysis")
st.write("6️⃣ Exploratory Data Analysis")
st.write("7️⃣ Multiple Regression Models")
st.write("8️⃣ Model Performance Comparison")
st.write("9️⃣ Actual vs Predicted Analysis")
st.write("🔟 Feature Importance Analysis")

st.markdown("---")
st.header("📂 Dataset")
st.write("""
**Dataset Used:**
- Advertising Dataset

**Dataset Size:**
- **200 records**

**Input Features:**
- TV
- Radio
- Newspaper

**Target Variable:**
- Sales
""")

st.markdown("---")
st.header("🤖 Machine Learning Model")
st.write("""
**Algorithms Tested**

• Linear Regression

• Decision Tree Regressor

• Random Forest Regressor

**Model Selection**

The models are compared using MAE, RMSE, and R² Score.
The model with the highest R² Score on the test data is selected
as the primary prediction model.
""")

st.markdown("---")
st.header("📚 Python Libraries")

libraries = [
    "Python",
    "Streamlit",
    "Pandas",
    "NumPy",
    "Scikit-Learn",
    "Matplotlib",
    "Seaborn",
]

col1, col2 = st.columns(2)

for i, library in enumerate(libraries):
    if i % 2 == 0:
        col1.write(f"✅ {library}")
    else:
        col2.write(f"✅ {library}")

st.markdown("---")
st.header("⚙️ Project Workflow")

st.write("1️⃣ Load the Advertising Dataset")
st.write("2️⃣ Clean the Data")
st.write("3️⃣ Remove Duplicate Records")
st.write("4️⃣ Perform Exploratory Data Analysis")
st.write("5️⃣ Analyze Feature Correlation")
st.write("6️⃣ Split Data into Training and Testing Sets")
st.write("7️⃣ Train Regression Models")
st.write("8️⃣ Evaluate Model Performance")
st.write("9️⃣ Select the Best Model")
st.write("🔟 Predict Sales")

st.markdown("---")
st.header("📁 Project Modules")
st.write("🏠 Home")
st.write("🔮 Predict Sales")
st.write("📊 Data Insights")
st.write("🤖 Model Performance")
st.write("📈 Feature Importance")
st.write("ℹ️ About")

st.markdown("---")
st.header("🔮 Future Improvements")
st.write("1️⃣ Add cross-validation")
st.write("2️⃣ Add hyperparameter tuning")
st.write("3️⃣ Add prediction confidence intervals")
st.write("4️⃣ Add more machine learning algorithms")
st.write("5️⃣ Add model download option")
st.write("6️⃣ Add interactive prediction history")
st.write("7️⃣ Add cloud deployment")
st.write("8️⃣ Add automatic model retraining")
st.write("9️⃣ Add support for larger and real-world datasets")
st.write("🔟 Add a REST API for sales predictions")

st.markdown("---")
st.header("👨‍💻 Developer")
st.success("Name : Pramod")
st.success("Project : Sales Prediction System")
st.success("Frontend : Streamlit")
st.success("Machine Learning : Scikit-Learn")
st.success("Language : Python")

st.markdown("---")
st.info("Thank you for using the Sales Prediction System!")

st.markdown(
    """
    <div style="text-align:center; font-size:18px;">
    Made with ❤️ by <b>Pramod</b>
    </div>
    """,
    unsafe_allow_html=True,
)
