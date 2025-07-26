 # string.py

# Q1: Count number of uppercase and lowercase letters in a string
def count_case(s):
    upper_count = sum(1 for ch in s if ch.isupper())
    lower_count = sum(1 for ch in s if ch.islower())
    print(f"Input string: {s}")
    print("Uppercase letters:", upper_count)
    print("Lowercase letters:", lower_count)

count_case("Hello World")
print("-" * 40)

# Q2: Check whether a given string is a palindrome
def is_palindrome(s):
    if s == s[::-1]:
        print(f"{s} is a Palindrome.")
    else:
        print(f"{s} is not a Palindrome.")

is_palindrome("madam")
is_palindrome("hello")
print("-" * 40)

# Q3: Return new string made of n copies of first 2 chars of original string (n = length of string)
def repeat_first_two_chars(s):
    if len(s) >= 2:
        result = s[:2] * len(s)
        print(f"Input: {s} => Output: {result}")
    else:
        print("String length must be at least 2.")

repeat_first_two_chars("Wipro")
print("-" * 40)

# Q4: Remove 'x' from start and end of string if present
def remove_x(s):
    if s.startswith('x'):
        s = s[1:]
    if s.endswith('x'):
        s = s[:-1]
    print(f"Processed string: {s}")

remove_x("xHix")
remove_x("Hellox")
remove_x("xHello")
remove_x("Hello")
print("-" * 40)

# Q5: Repeat last n characters of string, n times
def repeat_last_n_chars(s, n):
    if 0 <= n <= len(s):
        last_n = s[-n:]
        result = last_n * n
        print(f"Input: {s}, n={n} => Output: {result}")
    else:
        print("Invalid value of n.")

repeat_last_n_chars("Wipro", 3)
repeat_last_n_chars("Python", 2)