import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
n = 1000

# Generate synthetic data
product_id = np.arange(1, n+1)
base_price = np.round(np.random.uniform(20, 100, n), 2)
competitor_price = np.round(base_price + np.random.normal(0, 5, n), 2)
customer_rating = np.round(np.random.uniform(1, 5, n), 1)
demand_elasticity = np.round(np.random.uniform(-2, 0, n), 2)  # negative elasticity
seasonality = np.random.choice(['High', 'Medium', 'Low'], size=n)
marketing_spend = np.round(np.random.uniform(1000, 10000, n), 2)

# Simulate sales volume based on pricing and customer rating
sales_volume = (
    2000 +
    (customer_rating * 200) -
    (base_price * 10 * demand_elasticity) +
    np.random.normal(0, 200, n)
).astype(int)

# Cap sales_volume to positive integers
sales_volume = np.maximum(sales_volume, 0)

# Create dataframe
df = pd.DataFrame({
    'Product_ID': product_id,
    'Base_Price': base_price,
    'Competitor_Price': competitor_price,
    'Customer_Rating': customer_rating,
    'Demand_Elasticity': demand_elasticity,
    'Seasonality': seasonality,
    'Marketing_Spend': marketing_spend,
    'Sales_Volume': sales_volume
})

# Save to CSV
df.to_csv("bosch_pricing_optimization_dataset.csv", index=False)

print("✅ Dataset generated and saved as 'bosch_pricing_optimization_dataset.csv'")
