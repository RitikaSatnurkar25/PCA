import pandas as pd

# Load Flipkart data
flipkart_data = pd.read_csv("flipkart_name.csv")

# Display first few rows
print(flipkart_data.head())
comparison_data = []

for index, row in flipkart_data.iterrows():
    product_name = row["Product Name"]
    flipkart_price = row["Price"]
    
    # Assume you've scraped Amazon/Myntra price
    amazon_price = 300  # Example value
    myntra_price = 280  # Example value
    
    comparison_data.append({
        "Product Name": product_name,
        "Flipkart Price": flipkart_price,
        "Amazon Price": amazon_price,
        "Myntra Price": myntra_price
    })

# Convert to DataFrame
comparison_df = pd.DataFrame(comparison_data)
print(comparison_df)
comparison_df.to_csv("price_comparison.csv", index=False)
