import time
import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_myntra_products(product_name):
    # Initialize undetected ChromeDriver
    options = uc.ChromeOptions()
    options.headless = False  # Set to True to run in headless mode
    driver = uc.Chrome(options=options)
    
    try:
        # Open Myntra and search for the product
        driver.get("https://www.myntra.com/")
        search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "desktop-searchBar")))
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.RETURN)

        # Wait for results to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "product-base")))

        # Extract product details
        products = driver.find_elements(By.CLASS_NAME, "product-base")

        product_list = []
        for product in products:
            try:
                name = product.find_element(By.CLASS_NAME, "product-brand").text + " " + product.find_element(By.CLASS_NAME, "product-product").text
                price = product.find_element(By.CLASS_NAME, "product-discountedPrice").text if len(product.find_elements(By.CLASS_NAME, "product-discountedPrice")) > 0 else product.find_element(By.CLASS_NAME, "product-price").text
                price = int("".join(filter(str.isdigit, price)))  # Convert price to integer
                link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
                
                product_list.append({"Product Name": name, "Price": price, "Link": link})
            except Exception as e:
                print(f"Error extracting product: {e}")

        # Sort by price and get top 5
        product_list = sorted(product_list, key=lambda x: x["Price"])[:5]

        # Convert to DataFrame and save to CSV
        df = pd.DataFrame(product_list)
        df.to_csv("myntra_results.csv", index=False)

        return df

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    product_name = input("Enter the product name: ")
    results = get_myntra_products(product_name)
    print("\nMyntra Results:")
    print(results)
