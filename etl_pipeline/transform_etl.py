import pandas as pd

# Step 1: Extract
df = pd.read_csv("data/raw_sales.csv")

print("Raw Data:")
print(df.head())

# Step 2: Transform

# Clean column names
df.columns = [col.strip().lower() for col in df.columns]

# Convert date column
df['order_date'] = pd.to_datetime(df['order_date'])

# Create new columns
df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.month

# Revenue calculation
df['revenue'] = df['quantity'] * df['price']

# Remove bad records
df = df[df['quantity'] > 0]

# Step 3: Aggregation (Fact Table style)
fact_sales = df.groupby(['year', 'month', 'product']).agg({
    'revenue': 'sum',
    'quantity': 'sum'
}).reset_index()

# Step 4: Save transformed data
fact_sales.to_csv("output/fact_sales.csv", index=False)

print("Transformation complete ✅")
