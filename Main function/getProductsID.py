import re
import csv

# Read HTML code from an external file
with open('allProducts.html', 'r', encoding='utf-8') as file:
    html_code = file.read()

# Regular expression pattern to extract product IDs
pattern = r'/device-showcase/device/(\d+)'

# Find all product IDs using regex
product_ids = re.findall(pattern, html_code)

# Save the product IDs to a CSV file
existing_ids = set()

with open('product_ids.csv', 'a+', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        existing_ids.add(row[0])

    writer = csv.writer(file)
    for product_id in product_ids:
        if product_id not in existing_ids:
            writer.writerow([product_id])
            existing_ids.add(product_id)

print("Product IDs saved to product_ids.csv file.")