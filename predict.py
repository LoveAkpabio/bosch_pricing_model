import requests

# Define the URL for the prediction
url = 'http://3.12.153.160:5000/predict'

# Example input data for prediction
test_data = {
    "Base_Price": 199.99,
    "Competitor_Price": 189.99,
    "Customer_Rating": 4.3,
    "Demand_Elasticity": 1.1,
    "Seasonality": 0.8,
    "Marketing_Spend": 5000.0
}

# Send the POST request to the Flask API
response = requests.post(url, json=test_data)

# Print the response status code and prediction
print("Status Code:", response.status_code)
print("Prediction Response:", response.json())
