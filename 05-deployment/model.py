import pickle
from fastapi import FastAPI
from pydantic import BaseModel

# 1. Load the trained pipeline or (dv, model)
model_file = "pipeline_v1.bin"

with open(model_file, "rb") as f_in:
    model = pickle.load(f_in)

# 2. Define input schema using Pydantic
class Lead(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

# 3. Create FastAPI app
app = FastAPI(title="Lead Conversion Predictor")

# 4. Define prediction endpoint
@app.post("/predict")
def predict(lead: Lead):
    lead_dict = lead.dict()

    # If model is pipeline (DictVectorizer + LogisticRegression):
    y_pred = model.predict_proba([lead_dict])[0, 1]

    return {
        "subscription_probability": float(y_pred),
        "will_subscribe": bool(y_pred >= 0.5)
    }
