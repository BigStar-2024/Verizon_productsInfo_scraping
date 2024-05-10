import csv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import os

# Check if the 'Products_info_imgurl.csv' file exists
if os.path.exists('Products_info_imgurl.csv'):
    # If the file exists, delete its contents
    with open('Products_info_imgurl.csv', 'w', newline='', encoding='utf-8') as file:
        # Open the file in write mode to truncate its contents
        pass

# Create the CSV file if it doesn't exist
with open('Products_info_imgurl.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(['Product ID', 'Img_URL'])

with open('product_ids.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file) 
    for row in reader:
        product_id = row[0]
        # url = f"https://opendevelopment.verizonwireless.com/device-showcase/device/{product_id}"
        url = f"https://odi-device.verizonwireless.com/odi/showcase/api/images/get/{product_id}"
        img_url = [url]

        # response = requests.get(url)
        # if response.status_code == 200:
        #     print(f"Successfully visited URL: {url}")
        # else:
        #     print(f"Failed to visit URL: {url}")

        # # initialize the Chrome driver
        # driver = webdriver.Chrome()
        # driver.maximize_window()

        # # head to product page
        # driver.get(url)

        # time.sleep(2)

        try:
            # # Find the img tag with class 'details__image' and get the src attribute
            # device_img_element = driver.find_element(By.CLASS_NAME, 'details__image-container')
            # img_element = device_img_element.find_element(By.CLASS_NAME, 'details__image')
            # src_url = [img_element.get_attribute('src')]
            # print(src_url)

                       
            # Save the extracted information to a CSV file
            with open('Products_info_imgurl.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(img_url)
        except NoSuchElementException:
            print(f"Could not find device subtitle or title for {url}")

        # # Close the browser window
        # driver.quit()
        # print("===============")

# print("Information scraped and saved to verizon_device_info.csv")