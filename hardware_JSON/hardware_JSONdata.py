import pandas as pd
import json

# List of encodings to try
encodings = ['utf-8', 'latin1', 'iso-8859-1']

# Try reading the CSV file with different encodings
for encoding in encodings:
    try:
        df = pd.read_csv('10products.csv', encoding=encoding)
        print("CSV file read successfully with encoding:", encoding)
        break
    except UnicodeDecodeError:
        print("Error reading CSV file with encoding:", encoding)

# Extract data from the third to fifth columns
data = df.iloc[:, 19:48]

# Convert the extracted data to JSON format
json_data = data.to_json(orient='records')
# Replace "\u0097" with "false" in the JSON data
json_data = json_data.replace("\\u0097", "False")
print(json_data)

# Load JSON data
data = json.loads(json_data)

# Extract the first column data
first_column_data = [{"First_Column": json.dumps(row)} for row in data]

# Create a DataFrame from the extracted data
df = pd.DataFrame(first_column_data)

# Save the DataFrame to a CSV file
df.to_csv('output.csv', index=False )

print("First column data saved to output.csv.")