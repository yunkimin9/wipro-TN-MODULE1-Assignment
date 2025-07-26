''' Project-1
Q 1-> Write a python function that accepts a hypen seprated sequence of colors as input and returns 
the colors in a hyphen-seprated sequence afte sorting them alphabetically.
''' 

def sort_colors(color_sequence):
    """
    Accepts a hyphen-separated color string, sorts the colors alphabetically,
    and returns the sorted hyphen-separated string.
    """
    
    color_list = color_sequence.split('-')

    color_list.sort()

    return '-'.join(color_list)


# --- Sample Execution ---
if __name__ == "__main__":
    user_input = input("Enter hyphen-separated color names: ")
    sorted_colors = sort_colors(user_input)
    print("Sorted colors:", sorted_colors)

''' Project-2
Q 2-> Create a python module with th following functions:
ispalindrome(name),count_the_vowels(name), frequency_of_letters(name).
name will be completely in either lower case or upper case. import the module in another python
script and test the function by passing appropriate inputs.
'''

from strings_util import ispalindrome, count_the_vowels, frequency_of_letters

name = input("Enter the name: ")

if ispalindrome(name):
    print("Yes it is a palindrome.")
else:
    print("No it is not a palindrome.")

vowel_count = count_the_vowels(name)
print(f"No of vowels: {vowel_count}")

freq = frequency_of_letters(name)
print("Frequency of letters:")
for char, count in sorted(freq.items()):
    print(f"{char}-{count}", end=", ")