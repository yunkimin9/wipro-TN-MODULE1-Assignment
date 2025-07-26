 # dictionary.py

# Q1: Add a key and value to a dictionary
sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30
print("After adding a key-value pair:", sample_dict)

print("-" * 40)

# Q2: Concatenate multiple dictionaries into one
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
concatenated_dict = {}
for d in (dic1, dic2, dic3):
    concatenated_dict.update(d)
print("Concatenated dictionary:", concatenated_dict)

print("-" * 40)

# Q3: Check if a given key exists in a dictionary
check_key = 3
if check_key in concatenated_dict:
    print(f"Key {check_key} exists in the dictionary.")
else:
    print(f"Key {check_key} does not exist in the dictionary.")

print("-" * 40)

# Q4: Iterate over a dictionary and print keys, values, and items
print("Keys:")
for key in concatenated_dict:
    print(key)

print("Values:")
for value in concatenated_dict.values():
    print(value)

print("Key-Value Pairs:")
for key, value in concatenated_dict.items():
    print(f"{key}: {value}")

print("-" * 40)

# Q5: Dictionary where keys are 1 to 15 and values are their squares
squares_dict = {x: x**2 for x in range(1, 16)}
print("Dictionary of squares from 1 to 15:")
print(squares_dict)

print("-" * 40)

# Q6: Sum of all values in a dictionary
total_sum = sum(concatenated_dict.values())
print("Sum of all values in the concatenated dictionary:", total_sum)