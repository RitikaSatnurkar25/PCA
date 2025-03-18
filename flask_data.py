from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# Function to load CSV data
def load_csv(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path).to_dict(orient='records')
    return []

@app.route("/", methods=["GET", "POST"])
def index():
    amazon_data, flipkart_data, myntra_data = [], [], []

    if request.method == "POST":
        search_term = request.form["product"]
        
        # Call scraping functions (Assuming they generate CSV files)
        os.system(f"python amazon_scraper.py '{search_term}'")
        os.system(f"python flipkart_scraper.py '{search_term}'")
        os.system(f"python myntra_scraper.py '{search_term}'")

        # Load CSV files into dictionaries
        amazon_data = load_csv("amazon_results.csv")
        flipkart_data = load_csv("flipkart_results.csv")
        myntra_data = load_csv("myntra_results.csv")

    return render_template("index.html", amazon=amazon_data, flipkart=flipkart_data, myntra=myntra_data)

if __name__ == "__main__":
    app.run(debug=True)
