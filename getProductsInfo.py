import csv
import requests

#Read product IDs from the CSV file
with open('product_ids.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  #Skip the header row
    for row in reader:
        product_id = row[0]
        url = f"https://opendevelopment.verizonwireless.com/device-showcase/device/{product_id}"

        #Send an HTTP GET request to the URL
        response =requests.get(url)

        #Check if the request was successful (status code 200)
        if response.status_code == 200:
            print(f"Successfully visited URL: {url}")
        else:
            print(f"Failed to visit URL: {url}")