from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load the model
model = joblib.load('regression.joblib')

class HouseFeatures(BaseModel):
    size: float
    bedrooms: int
    has_garden: bool

@app.post("/predict")
async def predict(features: HouseFeatures):
    try:
        # Prepare the input data
        input_data = [[features.size, features.bedrooms, int(features.has_garden)]]
        
        # Make prediction
        prediction = model.predict(input_data)
        
        return {"predicted_price": float(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
