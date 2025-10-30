import pickle

# 1. Load the trained pipeline
with open("pipeline_v1.bin", "rb") as f:
    model = pickle.load(f)

# 2. Prepare the input record
record = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

# 3. Predict the probability of conversion
# predict_proba returns two probabilities: [P(class=0), P(class=1)]
proba = model.predict_proba([record])[0, 1]

# 4. Print the result
print("Probability of conversion:", proba)
