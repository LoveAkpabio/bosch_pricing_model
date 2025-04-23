from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import joblib
import pandas as pd

app = Flask(__name__)

# Enable CORS for all domains
CORS(app)

# Load model
model = joblib.load('pricing_model.pkl')
# If you used a preprocessor:
# preprocessor = joblib.load('preprocessor.pkl')

@app.route('/')
def home():
    return "Bosch Pricing Optimization API is running"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the request
        data = request.get_json()

        # Ensure all the required keys are present in the request
        required_keys = ['Base_Price', 'Competitor_Price', 'Customer_Rating', 'Demand_Elasticity', 'Seasonality', 'Marketing_Spend']
        if not all(key in data for key in required_keys):
            return jsonify({'error': 'Missing required data in request'}), 400  # Return error if any key is missing

        # Extract features
        features = [
            data['Base_Price'],
            data['Competitor_Price'],
            data['Customer_Rating'],
            data['Demand_Elasticity'],
            data['Seasonality'],
            data['Marketing_Spend']
        ]
        
        # Predict using the loaded model
        prediction = model.predict([features])

        # Return the prediction
        return jsonify({'predicted_sales_volume': prediction[0]})

    except Exception as e:
        # Return error message in case of an exception
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
