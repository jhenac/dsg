from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

data = {
    'title': [],
    'url': [],
    'image': [],
    'price': []
}

url_list = []

chrome_driver = Service()
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
browser = webdriver.Chrome(service=chrome_driver, options=chrome_options)

browser.get('https://www.dickssportinggoods.com/f/shop-all-game-room-games?pageSize=144&pageNumber=5')
time.sleep(5)

# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")  
# time.sleep(3)  

titles = browser.find_elements(By.CSS_SELECTOR, 'a.rs_product_description')
prices = browser.find_elements(By.CSS_SELECTOR, 'div.rs_product_price')
images = browser.find_elements(By.CSS_SELECTOR, 'span.product-image-span img')

for title in titles:
    res = title.text
    data['title'].append(res)
    url = title.get_attribute('href')
    data['url'].append(url)

for image in images:
    res = image.get_attribute('src')
    data['image'].append(res)

for price in prices:
    res = price.text
    data['price'].append(res)

browser.close()

print(data)

df = pd.DataFrame.from_dict(data)

df.to_csv('outdoor_2.csv', mode='a', index=False, header=False)