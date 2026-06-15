import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os

app = FastAPI(title="Salary Predictor API")

# Define the data format expected from the Frontend
class PredictRequest(BaseModel):
    years_experience: float

# Define the output format
class PredictResponse(BaseModel):
    predicted_salary: float

# Attempt to load the pre-trained Pickle file when the server starts
def load_model():
    model_path = r"D:\innomatic training notes\model_building\training\demo_project\salary_prediction_app\backend\salary_model.pkl"
    if os.path.exists(model_path):
        return joblib.load(model_path)
    return None

ml_model = load_model()

@app.post("/predict", response_model=PredictResponse)
def predict_salary(request: PredictRequest):
    if ml_model is None:
        raise HTTPException(
            status_code=500, 
            detail="The ML model file 'salary_model.pkl' could not be found! Please download it from Colab and drop it in this backend folder."
        )
    
    # Scikit-learn expects a 2D array: [[years_experience]]
    prediction = ml_model.predict([[request.years_experience]])
    
    # Return the first element of the prediction array
    return PredictResponse(predicted_salary=round(prediction[0], 2))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
