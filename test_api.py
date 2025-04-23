import requests

# This is your Flask app URL
url = "http://127.0.0.1:5000/predict"

# Test input data – must match your model's features!
data = {
    "Base_Price": 200.0,
    "Competitor_Price": 190.0,
    "Customer_Rating": 4.5,
    "Demand_Elasticity": 0.8,
    "Seasonality": 1.0,
    "Marketing_Spend": 15000.0
}

# Send the data as a POST request to your Flask app
response = requests.post(url, json=data)

# Show the result (prediction)
print(response.json())
