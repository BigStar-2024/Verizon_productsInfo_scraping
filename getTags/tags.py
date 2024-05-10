import csv

# Open the input CSV file
with open('tags.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

# Merge the three columns into a single column
merged_rows = []
for row in rows:
    merged_column = ', '.join(row[:3])  # Merge the first three columns
    merged_row = [merged_column] + row[3:]  # Append the remaining columns
    merged_rows.append(merged_row)

# Open the output CSV file and write the merged data
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(merged_rows)
