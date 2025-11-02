import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
import joblib

# Create Flask app
app = Flask(__name__)

# Load trained model
model = joblib.load("drug-recommender.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)  # Receive JSON from Streamlit
    Age = data['age']
    Male = 1 if data['gender'] == 'male' else 0
    Cholesterol_Status = 1 if data['cholesterol'] == 'cholesterolHigh' else 0

    BP = data['bp']
    if BP == 'bpHigh':
        BP_HIGH = 1
        BP_LOW = 0
    elif BP == 'bpLow':
        BP_HIGH = 0
        BP_LOW = 1
    else:
        BP_HIGH = 0
        BP_LOW = 0

    NatoKBox = data['na_to_k']

    # Predict
    prediction = model.predict([[Age, Male, Cholesterol_Status, NatoKBox, BP_HIGH, BP_LOW]])
    
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
