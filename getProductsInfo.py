import csv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with open('product_ids.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header_written = False
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

            # Save the extracted information to a CSV file
            with open('Products_info.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                if not header_written:
                    writer.writerow(['Device Subtitle'])
                    header_written = True
                writer.writerow([device_subtitle])
        except NoSuchElementException: # type: ignore
            print(f"Could not find device subtitle for {url}")

        # Close the browser window
        driver.quit()

print("Information scraped and saved to verizon_device_info.csv")