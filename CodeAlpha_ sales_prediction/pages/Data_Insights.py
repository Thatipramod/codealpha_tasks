import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from model_utils import load_data, train_models

# Page Configuration
st.set_page_config(page_title="Data Insights", page_icon="📊", layout="wide")


# Load Cleaned Data
@st.cache_data
def get_data():
    return load_data("cleaned_data.csv")


# Train Models
@st.cache_resource
def get_models(df):
    return train_models(df)


# Load Data and Models
df = get_data()
model, model_name, results_df, y_test, predictions = get_models(df)

st.title("📊 Data Insights")
st.write(
    "Explore the data and understand the relationships between advertising and sales."
)
st.divider()


# Create Charts
def show_plot(kind, x, y=None, title="", xlabel="", ylabel=""):
    fig, ax = plt.subplots(figsize=(6, 4))

    if kind == "hist":
        sns.histplot(df[x], kde=True, ax=ax)
    else:
        sns.scatterplot(data=df, x=x, y=y, ax=ax)

    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
    st.pyplot(fig)
    plt.close(fig)


col1, col2 = st.columns(2)


# Left Column
with col1:
    st.subheader("Sales Distribution")
    show_plot(
        "hist", "Sales", title="Sales Distribution", xlabel="Sales", ylabel="Frequency"
    )
    st.caption(
        "Sales values are mainly concentrated around the middle range, with fewer observations at very low and very high levels."
    )

    st.subheader("TV Advertising vs Sales")
    show_plot(
        "scatter",
        "TV",
        "Sales",
        title="TV Advertising vs Sales",
        xlabel="TV Advertising",
        ylabel="Sales",
    )
    st.caption("TV advertising shows a strong positive relationship with Sales.")

    st.subheader("Radio Advertising vs Sales")
    show_plot(
        "scatter",
        "Radio",
        "Sales",
        title="Radio Advertising vs Sales",
        xlabel="Radio Advertising",
        ylabel="Sales",
    )
    st.caption(
        "Radio advertising shows a positive relationship with Sales, but the points are more spread out than TV."
    )

    st.subheader("Newspaper Advertising vs Sales")
    show_plot(
        "scatter",
        "Newspaper",
        "Sales",
        title="Newspaper Advertising vs Sales",
        xlabel="Newspaper Advertising",
        ylabel="Sales",
    )
    st.caption(
        "Newspaper advertising has a weaker relationship with Sales compared with TV and Radio."
    )

    st.subheader("Total Advertising vs Sales")
    show_plot(
        "scatter",
        "Total_Advertising",
        "Sales",
        title="Total Advertising vs Sales",
        xlabel="Total Advertising",
        ylabel="Sales",
    )
    st.caption(
        "Higher overall advertising spending is generally associated with higher Sales."
    )


# Right Column
with col2:
    st.subheader("Correlation Matrix")

    corr = df[["TV", "Radio", "Newspaper", "Sales"]].corr()
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Matrix")
    st.pyplot(fig)
    plt.close(fig)

    st.caption(
        "TV has the strongest correlation with Sales, followed by Radio, while Newspaper has a weaker correlation."
    )

    st.subheader("Actual vs Predicted Sales")

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(y_test, predictions)
    ax.set(
        title=f"Actual vs Predicted Sales ({model_name})",
        xlabel="Actual Sales",
        ylabel="Predicted Sales",
    )
    st.pyplot(fig)
    plt.close(fig)

    st.caption(
        "Points closer to a diagonal pattern indicate more accurate predictions."
    )

    st.subheader("Prediction Error Analysis")

    error = y_test - predictions
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(error, kde=True, ax=ax)
    ax.set(
        title="Prediction Error Analysis", xlabel="Prediction Error", ylabel="Frequency"
    )
    st.pyplot(fig)
    plt.close(fig)

    st.caption(
        "Errors centered around zero indicate that predictions are generally close to actual Sales values."
    )

    st.subheader("Feature Importance")

    if hasattr(model, "feature_importances_"):
        importance = pd.Series(
            model.feature_importances_, index=["TV", "Radio", "Newspaper"]
        ).sort_values()

        fig, ax = plt.subplots(figsize=(6, 4))
        importance.plot(kind="barh", ax=ax)
        ax.set(
            title=f"Feature Importance ({model_name})",
            xlabel="Importance",
            ylabel="Feature",
        )
        st.pyplot(fig)
        plt.close(fig)

        st.caption(
            "Higher importance means the feature contributes more to the model's Sales predictions."
        )
    else:
        st.info("Feature importance is available for tree-based models.")
