import csv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import os

# Check if the 'Products_info.csv' file exists
if os.path.exists('Products_info.csv'):
    # If the file exists, delete its contents
    with open('Products_info.csv', 'w', newline='', encoding='utf-8') as file:
        # Open the file in write mode to truncate its contents
        pass

# Create the CSV file if it doesn't exist
with open('Products_info.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(['Device Subtitle', 'Device Title'])

with open('product_ids.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file) 
    for row in reader:
        product_id = row[0]
        url = f"https://opendevelopment.verizonwireless.com/device-showcase/device/{product_id}"

        response = requests.get(url)
        if response.status_code == 200:
            print(f"Successfully visited URL: {url}")
        else:
            print(f"Failed to visit URL: {url}")

        # initialize the Chrome driver
        driver = webdriver.Chrome()
        driver.maximize_window()

        # head to product page
        driver.get(url)

        time.sleep(2)

        try:
            device_subtitle_element = driver.find_element(By.CSS_SELECTOR, ".details__content-subtitle a")
            device_subtitle = device_subtitle_element.text
            print(device_subtitle)

            device_title_element = driver.find_elements(By.CSS_SELECTOR, ".details__content-title")
            device_title = device_title_element[1].text
            print(device_title)

            # Save the extracted information to a CSV file
            with open('Products_info.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([device_subtitle, device_title])
        except NoSuchElementException:
            print(f"Could not find device subtitle or title for {url}")

        # Close the browser window
        driver.quit()

print("Information scraped and saved to verizon_device_info.csv")