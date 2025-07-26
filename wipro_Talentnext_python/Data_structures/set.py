 # set.py

# Q1: Remove a given item from the set
my_set = {10, 20, 30, 40, 50}
print("Original set:", my_set)
item_to_remove = 30
my_set.discard(item_to_remove)  # discard avoids error if item not found
print(f"Set after removing {item_to_remove}:", my_set)

print("-" * 40)

# Q2: Create an intersection of sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection_result = set1 & set2
print("Intersection of sets:", intersection_result)

print("-" * 40)

# Q3: Create a union of sets
union_result = set1 | set2
print("Union of sets:", union_result)

print("-" * 40)

# Q4: Find the maximum and minimum value in a set
num_set = {12, 45, 23, 67, 89, 5}
print("Set:", num_set)
print("Maximum value in the set:", max(num_set))
print("Minimum value in the set:", min(num_set))