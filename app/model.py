import joblib

model = joblib.load("model/model.pkl")

def predict(data):
    """
    data: list of features in correct order
    """
    prediction = model.predict([data])
    return prediction[0]
