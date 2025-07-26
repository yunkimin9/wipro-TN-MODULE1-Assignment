 # lists.py

# Q1: Create a list of 5 integers and display the list items. Access individual elements through index.
int_list = [10, 20, 30, 40, 50]
print("List items:", int_list)
print("Access by index:")
for i in range(len(int_list)):
    print(f"Element at index {i}:", int_list[i])

print("-" * 40)

# Q2: Append a new item to the end of the list.
int_list.append(60)
print("After appending 60:", int_list)

print("-" * 40)

# Q3: Reverse the order of the items in the list.
int_list.reverse()
print("After reversing:", int_list)

print("-" * 40)

# Q4: Print the number of occurrences of a specified element in a list.
element = 30
count = int_list.count(element)
print(f"Number of occurrences of {element}:", count)

print("-" * 40)

# Q5: Append the items of list1 to list2 in the front.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# Prepending list1 to list2
list2 = list1 + list2
print("After prepending list1 to list2:", list2)

print("-" * 40)

# Q6: Insert a new item before the second element in an existing list.
new_item = 99
int_list.insert(1, new_item)
print("After inserting 99 before second element:", int_list)

print("-" * 40)

# Q7: Remove the item from a specified index in a list.
remove_index = 3
if 0 <= remove_index < len(int_list):
    removed_item = int_list.pop(remove_index)
    print(f"After removing item at index {remove_index} ({removed_item}):", int_list)
else:
    print("Invalid index to remove.")

print("-" * 40)

# Q8: Remove the first occurrence of a specified element from a list.
remove_element = 50
if remove_element in int_list:
    int_list.remove(remove_element)
    print(f"After removing first occurrence of {remove_element}:", int_list)
else:
    print(f"{remove_element} not found in the list.")