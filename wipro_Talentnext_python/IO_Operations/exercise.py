 # Q1: Read the entire content from a txt file and display it
file_path = "sample.txt"  
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print("Full file content:\n", content)
except FileNotFoundError:
    print("File not found.")

# Q2: Read first n lines from a txt file
n = int(input("Enter the number of lines to read: "))
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        for i in range(n):
            line = file.readline()
            if not line:
                break
            print(line.strip())
except FileNotFoundError:
    print("File not found.")

# Q3: Accept input from user and append it to a txt file
user_text = input("Enter text to append to the file: ")
try:
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(user_text + "\n")
    print("Text appended successfully.")
except FileNotFoundError:
    print("File not found.")

# Q4: Read file line by line and store each line into a list
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines_list = [line.strip() for line in file.readlines()]
    print("Lines as list:", lines_list)
except FileNotFoundError:
    print("File not found.")

# Q5: Find the longest word in the file
import re

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text)
        longest_word = max(words, key=len)
    print("Longest word:", longest_word)
except FileNotFoundError:
    print("File not found.")

# Q6: Count frequency of a user-entered word in the file
search_word = input("Enter the word to search for: ").lower()
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        count = words.count(search_word)
    print(f"The word '{search_word}' appears {count} times.")
except FileNotFoundError:
    print("File not found.")