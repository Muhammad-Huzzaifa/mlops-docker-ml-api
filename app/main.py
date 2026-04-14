from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict

app = FastAPI()

class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.get("/")
def home():
    return {"message": "ML API is running"}

@app.post("/predict")
def get_prediction(features: HouseFeatures):
    
    input_data = [
        features.MedInc,
        features.HouseAge,
        features.AveRooms,
        features.AveBedrms,
        features.Population,
        features.AveOccup,
        features.Latitude,
        features.Longitude
    ]
    
    result = predict(input_data)

    return {
        "predicted_house_price": result
    }
