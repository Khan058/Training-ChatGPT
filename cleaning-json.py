import json

# Replace 'your_input_file.json' with the path to your input JSON file
input_file = 'your_input_file.json'

# Replace 'your_output_file.json' with the path to your output JSON file
output_file = 'your_output_file.json'

# Replace 'word1' and 'word2' with the words you want to remove
words_to_remove = ['word1' 'word2']

# A recursive function to remove target words from the data
def remove_words(obj, words):
    # If the input object is a list, recursively call the function on each item in the list
    if isinstance(obj, list):
        return [remove_words(item, words) for item in obj]
    # If the input object is a dictionary, recursively call the function on each key-value pair
    elif isinstance(obj, dict):
        return {key: remove_words(value, words) for key, value in obj.items()}
    # If the input object is a string, remove target words from the string
    elif isinstance(obj, str):
        for word in words:
            obj = obj.replace(word, '')
        return obj
    # If the input object is not a list, dictionary, or string, return the object as is
    else:
        return obj



# Read the input JSON file line by line and decode each line as a separate JSON object
data = []
with open(input_file, 'r') as f:
    for line in f:
        data.append(json.loads(line.strip()))

# Remove the target words from the data
modified_data = [remove_words(item, words_to_remove) for item in data]

# Write the modified data back to the JSON file as newline-delimited JSON
with open(output_file, 'w') as f:
    for item in modified_data:
        json.dump(item, f)
        f.write('\n')

#Print the result
print(f"Words {words_to_remove} have been removed from {input_file} and saved to {output_file}")
