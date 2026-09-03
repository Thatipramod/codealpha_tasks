# Importing Libraries
import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# Load Data
df = pd.read_csv("Advertising.csv")

# Display Top 5 Rows
print(df.head())

# Display Bottom 5 Rows
print(df.tail())

# Display Shape of Dataset
print(df.shape)

# Display Information About Dataset
df.info()

# Remove Unnecessary Column
df = df.drop("Unnamed: 0", axis=1)

# Display Statistical Summary
print(df.describe())

# Display Columns
print("Columns")
print(df.columns)

# Check Missing Values
print(df.isnull().sum())

# Check Duplicate Rows
print(df.duplicated().sum())

# Remove Duplicate Rows
df.drop_duplicates(inplace=True)

# Display Data Types
print(df.dtypes)


# Save Cleaned Data
df.to_csv("cleaned_data.csv", index=False)
print("Cleaned data saved successfully")


# Analyze Sales Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Sales"], kde=True)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.savefig("images/sales_distribution.png", bbox_inches="tight")
plt.show()
plt.close()


# TV Advertising vs Sales
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="TV", y="Sales")
plt.title("TV Advertising vs Sales")
plt.xlabel("TV")
plt.ylabel("Sales")
plt.savefig("images/tv_vs_sales.png", bbox_inches="tight")
plt.show()
plt.close()


# Radio Advertising vs Sales
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Radio", y="Sales")
plt.title("Radio Advertising vs Sales")
plt.xlabel("Radio")
plt.ylabel("Sales")
plt.savefig("images/radio_vs_sales.png", bbox_inches="tight")
plt.show()
plt.close()


# Newspaper Advertising vs Sales
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Newspaper", y="Sales")
plt.title("Newspaper Advertising vs Sales")
plt.xlabel("Newspaper")
plt.ylabel("Sales")
plt.savefig("images/newspaper_vs_sales.png", bbox_inches="tight")
plt.show()
plt.close()


# Correlation Analysis
plt.figure(figsize=(8, 5))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.savefig("images/correlation_matrix.png", bbox_inches="tight")
plt.show()
plt.close()


# Display Correlation with Sales
print(df.corr()["Sales"].sort_values(ascending=False))


# Create Total Advertising Feature
df["Total_Advertising"] = df["Newspaper"] + df["TV"] + df["Radio"]

# Save cleaned data again after creating the new feature
df.to_csv("cleaned_data.csv", index=False)


# Total Advertising vs Sales
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Total_Advertising", y="Sales")
plt.title("Total Advertising vs Sales")
plt.xlabel("Total Advertising")
plt.ylabel("Sales")
plt.savefig("images/total_advertising_vs_sales.png", bbox_inches="tight")
plt.show()
plt.close()


# Define X and Y
x = df[["TV", "Newspaper", "Radio"]]
y = df["Sales"]


# Train and Test Split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.20, random_state=42
)


# Linear Regression
linear_model = LinearRegression()
linear_model.fit(x_train, y_train)
linear_pred = linear_model.predict(x_test)


# Decision Tree
tree_model = DecisionTreeRegressor(random_state=42)
tree_model.fit(x_train, y_train)
tree_pred = tree_model.predict(x_test)


# Random Forest
rf_model = RandomForestRegressor(random_state=42, n_estimators=200)
rf_model.fit(x_train, y_train)
rf_pred = rf_model.predict(x_test)


# Evaluate Model
def evaluate_model(name, actual, predicted):
    mae = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    r2 = r2_score(actual, predicted)

    return {"Model": name, "MAE": mae, "RMSE": rmse, "R2 Score": r2}


# Store Model Results
result = []

result.append(evaluate_model("Linear Regression", y_test, linear_pred))

result.append(evaluate_model("Decision Tree", y_test, tree_pred))

result.append(evaluate_model("Random Forest", y_test, rf_pred))


# Create Results DataFrame
results_df = pd.DataFrame(result)
results_df["R2_percentage"] = results_df["R2 Score"] * 100


# Display Model Comparison
print("\nModel Comparison:")
print(results_df)


# Best model
best_model = results_df.loc[results_df["R2 Score"].idxmax()]

print("\nBest Model:")
print(best_model)


# Actual vs predicted
plt.figure(figsize=(8, 5))
plt.scatter(y_test, rf_pred)
plt.title("Actual vs Predicted")
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.savefig("images/actual_vs_predicted.png", bbox_inches="tight")
plt.show()
plt.close()


# Predicted Error Analysis
error = y_test - rf_pred

plt.figure(figsize=(8, 5))
sns.histplot(error, kde=True)
plt.title("Prediction Error Analysis")
plt.xlabel("Prediction Error")
plt.savefig("images/prediction_error_analysis.png", bbox_inches="tight")
plt.show()
plt.close()


# Feature Importance
importance = pd.Series(rf_model.feature_importances_, index=x.columns)

importance.sort_values(ascending=False)


# Plotting
importance.sort_values(ascending=True).plot(kind="barh", figsize=(8, 5))

plt.title("Advertising Feature Importance")
plt.savefig("images/feature_importance.png", bbox_inches="tight")
plt.show()
plt.close()


# Save the best model
joblib.dump(rf_model, "models/sales_prediction_model.pkl")

print("Model saved successfully")
print("Cleaned data saved as cleaned_data.csv")
print("All graphs saved inside images folder")
