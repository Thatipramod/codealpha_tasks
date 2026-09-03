import os
import streamlit as st
from model_utils import load_data, train_models

st.set_page_config(page_title="Model Performance", page_icon="🤖", layout="wide")


@st.cache_data
def get_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, "cleaned_data.csv")
    return load_data(DATA_PATH)


@st.cache_resource
def get_models(df):
    return train_models(df)


df = get_data()
model, best_model_name, results_df, y_test, predictions = get_models(df)

st.title("🤖 Model Performance")
st.write("Comparison of the regression models using test data.")
st.write("---")

display_df = results_df.copy()
display_df["MAE"] = display_df["MAE"].map("{:.4f}".format)
display_df["RMSE"] = display_df["RMSE"].map("{:.4f}".format)
display_df["R2 Score"] = display_df["R2 Score"].map("{:.4f}".format)

best_mae = results_df["MAE"].min()
best_rmse = results_df["RMSE"].min()
best_r2 = results_df["R2 Score"].max()
best_r2_percentage = results_df.loc[results_df["R2 Score"].idxmax(), "R2 Percentage"]


def highlight_best(row):
    styles = [""] * len(row)
    if results_df.loc[row.name, "MAE"] == best_mae:
        styles[display_df.columns.get_loc("MAE")] = (
            "background-color: #FFF3B0; color: #000000; font-weight: bold;"
        )
    if results_df.loc[row.name, "RMSE"] == best_rmse:
        styles[display_df.columns.get_loc("RMSE")] = (
            "background-color: #FFF3B0; color: #000000; font-weight: bold;"
        )
    if results_df.loc[row.name, "R2 Score"] == best_r2:
        styles[display_df.columns.get_loc("R2 Score")] = (
            "background-color: #FFF3B0; color: #000000; font-weight: bold;"
        )
        styles[display_df.columns.get_loc("R2 Percentage")] = (
            "background-color: #FFF3B0; color: #000000; font-weight: bold;"
        )
    return styles


styled_df = display_df.style.apply(highlight_best, axis=1)

st.dataframe(styled_df, use_container_width=True, hide_index=True)

st.success(f"🏆 Best Model: **{best_model_name}** | R² Score: **{best_r2_percentage}**")

st.write("---")
st.subheader("Understanding the Metrics")
st.write("""
**MAE (Mean Absolute Error)**
Measures the average difference between actual and predicted sales. Lower values are better.

**RMSE (Root Mean Squared Error)**
Gives more importance to larger prediction errors. Lower values are better.

**R² Score**
Shows how well the model explains the variation in Sales. Values closer to 1 are better.

**R² Percentage**
R² Score multiplied by 100 for easier presentation. It should not be treated as classification accuracy.
""")
