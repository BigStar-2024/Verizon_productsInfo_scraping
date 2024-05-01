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

    writer.writerow(['Device Subtitle', 'Device Title', 'Key Feature_1', 
                     'Key Feature_2', 'Key Feature_3', 'Key Feature_4', 'Key Feature_5', 'Key Feature_6', 
                     'Product description', 'Device Type', 'Network Technology', 'LTE catagory support',
                     'Contact_Address', 'Contact_Phone', 'Contact_Email'])

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
            # Device Subtitle
            device_subtitle_element = driver.find_element(By.CSS_SELECTOR, ".details__content-subtitle a")
            device_subtitle = device_subtitle_element.text
            print(device_subtitle)

            # Device title
            device_title_element = driver.find_elements(By.CSS_SELECTOR, ".details__content-title")
            device_title = device_title_element[1].text
            print(device_title)

            # Key Features
            key_feature_elements = driver.find_elements(By.CLASS_NAME, "details__content-item")
            key_features = [feature.text for feature in key_feature_elements]

            # Pad the key_features list with empty strings if there are fewer than 6 features
            while len(key_features) < 6:
                key_features.append('')
            print(key_features)

            # Product description
            product_description_element = driver.find_element(By.CLASS_NAME, "details__content-copy")
            product_description = [product_description_element.text]
            print(product_description)

            # Overview
            overview_elements = driver.find_elements(By.CLASS_NAME, "definition-list-description")
            ## Device Type
            overview_device_type = [overview_elements[0].text]
            print(overview_device_type)
            ## Network Technology
            overview_network_technology = [overview_elements[1].text]
            print(overview_network_technology)
            ## LTE Category Support
            overview_category_support = [overview_elements[2].text]
            print(overview_category_support)

            # Contact Manufacturer
            ## Sales
            contact_sales_elements = driver.find_elements(By.CSS_SELECTOR, ".details__image-content-copy-container p")
            contact_sales = [sales_element.text for sales_element in contact_sales_elements]
            print(contact_sales)
            ## Email
            contact_sales_email_element = driver.find_element(By.CSS_SELECTOR, ".details__image-content-copy-container a")
            contact_sales_email = [contact_sales_email_element.text]
            print(contact_sales_email)


            # Save the extracted information to a CSV file
            with open('Products_info.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([device_subtitle, device_title] + key_features + product_description + 
                                overview_device_type + overview_network_technology + overview_category_support + 
                                contact_sales + contact_sales_email)
        except NoSuchElementException:
            print(f"Could not find device subtitle or title for {url}")

        # Close the browser window
        driver.quit()

print("Information scraped and saved to verizon_device_info.csv")