import csv
import json

# Replace 'your_input_file.csv' with the path to your input CSV file
input_file = 'your_input_file.csv'

# Replace 'your_output_file.json' with the path to your output JSON file
output_file = 'your_output_file.json'

# Read the CSV file and store the data as a list of dictionaries
data = []
with open(input_file, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header row if present

# Replace or remove this section entrily if you need the whole file
#    counter = 0
#   for row in reader:
#        if counter >= 1000:
#           break

        obj = {
            # Replace 'column' with the number of colum from your file
            "prompt": row['column'],
            # Replace 'column' with the number of colum from your file
            "completion": row['column']
        }
        data.append(obj)
        counter += 1

# Write the data to the JSON file as newline-delimited JSON
with open(output_file, 'w') as f:
    for item in data:
        json.dump(item, f)
        f.write('\n')

#Print the result
print(
    f"CSV data from {input_file} has been converted to newline-delimited JSON and saved to {output_file}")
