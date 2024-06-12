import os
import requests
import uuid
import re
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Define the path to the ChromeDriver
CHROME_DRIVER_PATH = './chromedriver'

# Set up Chrome options to connect to an existing Chrome instance
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=chrome_options)

# List of URLs to scrape followers from
list_of_urls = [
    'https://x.com/pudgypenguins/followers',
    'https://x.com/ZelenskyyUa/followers',
    'https://x.com/BithumbOfficial/verified_followers',
    'https://x.com/OthersideMeta/followers',
    'https://x.com/elonmusk/verified_followers',
    'https://x.com/Azuki/followers',
    'https://x.com/Sololv_ARISE_GL/followers',
    'https://x.com/OnePieceAnime/followers'
]

# Directory to save images
images_dir = './images'
os.makedirs(images_dir, exist_ok=True)

# Data file to save user data
data_file = 'data.json'
if os.path.exists(data_file):
    with open(data_file, 'r') as f:
        data = json.load(f)
else:
    data = []

# Regular expression to allow only specific characters in usernames
allowed_characters = re.compile(r'^[\w\s\-@.,!?\'А-Яа-яЁё|]*$')

def scrape_followers():
    for url in list_of_urls:
        driver.get(url)
        time.sleep(5)
        print(driver.title)
        
        for i in range(50):
            if i % 10 == 0:
                print(i)
                driver.execute_script(f"window.scrollBy(0, {30*i})")
                time.sleep(3)
            
            try:
                user_name_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[{i+1}]/div/div/button/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]'))
                )
                
                user_name_text = user_name_element.text
                
                if not allowed_characters.match(user_name_text):
                    print(f"Skipping user with invalid characters: {user_name_text}")
                    continue
                
                image_element = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[{i+1}]/div/div/button/div/div[1]/div/div/div[2]/div/div[2]/div/a/div[3]/div/div[2]/div/img'))
                )
                
                try:
                    image_url = image_element.get_attribute('src').replace('normal', '400x400')
                    image_name = str(uuid.uuid4()) + '.jpg'
                    image_path = os.path.join(images_dir, image_name)
                    
                    img_data = requests.get(image_url).content
                    with open(image_path, 'wb') as handler:
                        handler.write(img_data)
                    
                    print(user_name_text, image_name)
                    
                    data.append((user_name_text, image_name))
                except Exception as e:
                    print(user_name_text, "No image", e)
                
            except Exception as e:
                print(f"Error finding element at index {i}: {e}")
                break
    
    driver.quit()

    with open(data_file, 'w') as f:
        json.dump(data, f, indent=4)

    print("Data saved successfully.")

if __name__ == '__main__':

    print("""
          

  _    _ _     _     _             _____          _      
 | |  | (_)   | |   | |           / ____|        | |     
 | |__| |_  __| | __| | ___ _ __ | |     ___   __| | ___ 
 |  __  | |/ _` |/ _` |/ _ \ '_ \| |    / _ \ / _` |/ _ \\
 | |  | | | (_| | (_| |  __/ | | | |___| (_) | (_| |  __/
 |_|  |_|_|\__,_|\__,_|\___|_| |_|\_____\___/ \__,_|\___|
                                                         
                   by Aero25x                                         
          
          """)

    scrape_followers()
