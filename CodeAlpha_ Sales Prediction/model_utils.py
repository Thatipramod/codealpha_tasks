import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


def load_data(file_path="cleaned_data.csv"):
    df = pd.read_csv(file_path)

    if "Unnamed: 0" in df.columns:
        df = df.drop("Unnamed: 0", axis=1)

    if "Total_Advertising" not in df.columns:
        df["Total_Advertising"] = df["Newspaper"] + df["TV"] + df["Radio"]

    return df


def train_models(df):
    X = df[["TV", "Radio", "Newspaper"]]
    y = df["Sales"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )

    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(random_state=42, max_depth=5),
        "Random Forest": RandomForestRegressor(
            n_estimators=200, max_depth=7, random_state=42
        ),
    }

    results = []
    trained_models = {}
    predictions = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        prediction = model.predict(X_test)

        trained_models[name] = model
        predictions[name] = prediction

        mae = mean_absolute_error(y_test, prediction)
        rmse = np.sqrt(mean_squared_error(y_test, prediction))
        r2 = r2_score(y_test, prediction)

        results.append(
            {
                "Model": name,
                "MAE": mae,
                "RMSE": rmse,
                "R2 Score": r2,
                "R2 Percentage": f"{r2 * 100:.2f}%",
            }
        )

    results_df = pd.DataFrame(results)
    best_index = results_df["R2 Score"].idxmax()
    best_model_name = results_df.loc[best_index, "Model"]

    return (
        trained_models[best_model_name],
        best_model_name,
        results_df,
        y_test,
        predictions[best_model_name],
    )
