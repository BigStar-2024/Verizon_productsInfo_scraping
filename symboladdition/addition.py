import pandas as pd

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

# Specify the columns from fifth to twelfth where you want to add "―" in front of the values
columns_to_update = df.columns[5:12]

# Add "―" in front of the values in the specified columns
df[columns_to_update] = '―' + df[columns_to_update].astype(str)
json_data = df
print(json_data)
# Replace "\u0097" with "false" in the JSON data
json_data = json_data.replace("―nan", "null")
json_data = json_data.replace("", "—")

# Save the updated DataFrame back to a CSV file
json_data.to_csv('updated_file.csv', index=False)

print("Values in the fifth to twelfth columns updated with '―' prefix and saved to updated_file.csv")