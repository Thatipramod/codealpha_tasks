import os
import pandas as pd
import streamlit as st
from model_utils import load_data, train_models

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "cleaned_data.csv")

st.set_page_config(page_title="Predict Sales", page_icon="🔮", layout="wide")


@st.cache_data
def get_data():
    return load_data(DATA_PATH)


@st.cache_resource
def get_models(_df):
    return train_models(_df)


df = get_data()
model, model_name, results_df, y_test, predictions = get_models(df)

st.title("🔮 Sales Prediction")
st.write("Enter the advertising budget for each channel to predict expected sales.")

tv = st.number_input("📺 TV Advertising ($k)", min_value=0.0, value=230.0, step=5.0)
radio = st.number_input("📻 Radio Advertising ($k)", min_value=0.0, value=37.0, step=2.0)
newspaper = st.number_input("📰 Newspaper Advertising ($k)", min_value=0.0, value=69.0, step=2.0)

total_advertising = tv + radio + newspaper
st.info(f"💰 Total Advertising Budget: ${total_advertising:.2f}k")

if st.button("🔮 Predict Sales", use_container_width=True, type="primary"):
    input_data = pd.DataFrame([[tv, radio, newspaper]], columns=["TV", "Radio", "Newspaper"])
    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("TV Advertising", f"${tv:.2f}k")
    with col2:
        st.metric("Radio Advertising", f"${radio:.2f}k")
    with col3:
        st.metric("Newspaper Advertising", f"${newspaper:.2f}k")

    st.success(f"📈 Predicted Sales: {prediction:.2f}k units")
    st.caption(f"Prediction generated using the {model_name} model.")
