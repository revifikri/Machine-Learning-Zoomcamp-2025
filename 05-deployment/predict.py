from fastapi import FastAPI
import pickle
from pydantic import BaseModel

app = FastAPI()

class Client(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

model_file = "/code/pipeline_v2.bin"
with open(model_file, "rb") as f_in:
    model = pickle.load(f_in)

@app.get("/")
def home():
    return {"message": "Lead conversion model is ready"}

@app.post("/predict")
def predict(client: Client):
    X = client.dict()
    prob = model.predict_proba([X])[0, 1]
    return {"conversion_probability": float(prob)}
