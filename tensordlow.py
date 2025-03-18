import os
from selenium.webdriver.chrome.options import Options
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-webgl")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument("--window-size=1920,1080")

