
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
import os
import undetected_chromedriver as uc

driver = uc.Chrome()


from selenium.webdriver.chrome.options import Options
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-webgl")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-software-rasterizer")




# Get user input for the search term
search_term = input("Enter the search term (e.g., laptop, phone): ")

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1920,1080")

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Limit the number of products to fetch per website
MAX_PRODUCTS = 5

# Function to clean price strings
def clean_price(price_text):
    return float(re.sub(r'[^\d.]', '', price_text))

# Function to display products
def display_products(site_name, products):
    print(f"\n--- {site_name} Results (Low to High, Top {MAX_PRODUCTS}) ---")
    for name, price, link in products[:MAX_PRODUCTS]:
        print(f"Product Name: {name}")
        print(f"Price: ₹{price}")
        print(f"Link: {link}")
        print("-" * 50)

# Amazon scraper
def scrape_amazon_in(search_term):
    url = f'https://www.amazon.in/s?k={search_term}'
    driver.get(url)
    time.sleep(2)

    product_names = driver.find_elements(By.CLASS_NAME, 'a-text-normal')
    product_prices = driver.find_elements(By.CLASS_NAME, 'a-price-whole')
    product_links = driver.find_elements(By.CLASS_NAME, 'a-link-normal')

    products = []
    for name, price, link in zip(product_names, product_prices, product_links):
        if len(products) >= MAX_PRODUCTS:
            break
        try:
            price_value = clean_price(price.text)
            product_link = re.search(r'(https://www\.amazon\.in/[^?]+)', link.get_attribute('href')).group(0)
            products.append((name.text, price_value, product_link))
        except (ValueError, AttributeError):
            continue

    products.sort(key=lambda x: x[1])
    display_products("Amazon India", products)



# Scrape all websites
try:
    scrape_amazon_in(search_term)
    
finally:
    driver.quit()
