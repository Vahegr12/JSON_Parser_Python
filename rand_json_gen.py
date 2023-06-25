import json
import random

def generate_json(max_depth):
    if max_depth == 0:
        return random.choice([1, 2, 3, 4, 5])  # Generate random leaf value

    data = {}
    num_items = random.randint(1, 5)  # Generate random number of items at this level
    for _ in range(num_items):
        key = f"key_{random.randint(1, 10)}"
        data[key] = generate_json(max_depth - 1)  # Recursive call to generate child level

    return data


def save_json_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


# Generate JSON data
max_depth = 3
json_data = generate_json(max_depth)

# Save JSON data to a file
filename = 'random_data.json'
save_json_file(json_data, filename)

print(f"Random JSON data saved to '{filename}' file.")
