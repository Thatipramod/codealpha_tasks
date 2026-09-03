import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from model_utils import load_data, train_models

# Page Configuration
st.set_page_config(page_title="Feature Importance", page_icon="📈", layout="wide")


# Load Cleaned Data
@st.cache_data
def get_data():
    return load_data("cleaned_data.csv")


# Train Models
@st.cache_resource
def get_models(df):
    return train_models(df)


# Load data and model
df = get_data()
model, model_name, results_df, y_test, predictions = get_models(df)


# Page Title
st.title("📈 Feature Importance")
st.write(f"This chart shows the importance of each feature in the {model_name} model.")


# Define Features
features = ["TV", "Radio", "Newspaper"]


# Get Feature Importance
if hasattr(model, "feature_importances_"):
    values = model.feature_importances_
    title = f"{model_name} Feature Importance"
    axis_label = "Importance"

elif hasattr(model, "coef_"):
    values = np.abs(model.coef_)
    title = f"{model_name} Feature Influence"
    axis_label = "Absolute Coefficient"

else:
    st.info("Feature importance is not available for this model.")
    st.stop()


# Create Importance DataFrame
importance_df = pd.DataFrame({"Feature": features, "Importance": values}).sort_values(
    "Importance"
)


# Create Feature Importance Chart
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(importance_df["Feature"], importance_df["Importance"])

ax.set_title(title)
ax.set_xlabel(axis_label)
ax.set_ylabel("Advertising Channel")


# Add Values to Bars
for bar in bars:
    value = bar.get_width()
    ax.text(
        value + 0.01, bar.get_y() + bar.get_height() / 2, f"{value:.3f}", va="center"
    )


# Display Chart
st.pyplot(fig)
plt.close(fig)


# Display Explanation
st.info(
    "A higher value means the feature has more influence on the model's predictions."
)
