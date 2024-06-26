import json

# Sample data
data = {
    "name": "Alice",
    "age": 30,
    "city": "Wonderland"
}

# File path
file_path = "data.json"

# Save data to a JSON file
def save_data(file_path, data):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print("Data saved to file.")

# Read data from a JSON file
def read_data(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

# Update data in a JSON file
def update_data(file_path, key, value):
    data = read_data(file_path)
    data[key] = value
    save_data(file_path, data)
    print("Data updated in file.")

# Example usage:
# Save initial data
save_data(file_path, data)

# Read data
loaded_data = read_data(file_path)
print("Loaded data:", loaded_data)

# Update data
update_data(file_path, "age", 31)

# Verify update
updated_data = read_data(file_path)
print("Updated data:", updated_data)
