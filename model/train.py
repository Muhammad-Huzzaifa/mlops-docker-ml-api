import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

data = fetch_california_housing()

df = pd.DataFrame(data.data, columns=data.feature_names)
df["price"] = data.target

X = df.drop("price", axis=1)
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, "model/model.pkl")

score = model.score(X_test, y_test)
print(f"Model trained successfully!")
print(f"R^2 Score: {score:.4f}")
