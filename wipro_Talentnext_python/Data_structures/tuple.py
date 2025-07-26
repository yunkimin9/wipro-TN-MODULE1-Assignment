 # tuple.py

# Q1: Print the 4th element from first and 4th from last in a tuple
my_tuple = (5, 10, 15, 20, 25, 30, 35, 40)
print("Tuple:", my_tuple)
print("4th element from start:", my_tuple[3])
print("4th element from end:", my_tuple[-4])

print("-" * 40)

# Q2: Check whether an element exists in a tuple
element = 25
if element in my_tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")

print("-" * 40)

# Q3: Convert a list into a tuple
my_list = [1, 2, 3, 4, 5]
converted_tuple = tuple(my_list)
print("Converted Tuple:", converted_tuple)

print("-" * 40)

# Q4: Find the index of an item in a tuple
item = 30
if item in my_tuple:
    index = my_tuple.index(item)
    print(f"Index of {item} in tuple:", index)
else:
    print(f"{item} is not in the tuple.")

print("-" * 40)

# Q5: Replace last value of tuples in a list to 100
sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print("Original list of tuples:", sample_list)
modified_list = [t[:-1] + (100,) for t in sample_list]
print("Modified list with last element replaced by 100:", modified_list)