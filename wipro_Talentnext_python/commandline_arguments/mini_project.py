''' Project-1 
Q-> Rhrough command line arguments three strings seprated by space are given to you.
each string is a series of numbers seprated by hyphen(-). you like all the numbers 
in string 1 and dislike all the numbers in string 2.
third string contains the numbers given to you. your initial happiness is 0.
when you encounter a number which is present in string 1, add 1 to your happiness, 
if it is present in string 2, and -1 to your happiness. otherwise, your happiness does not change.
output your final happiness at the end .  '''

import sys

def calculate_happiness():
    if len(sys.argv) != 4:
        print("Usage: python mini_project.py <like> <dislike> <given>")
        print("Example: python mini_project.py 3-1 5-7 1-5-3-8")
        return

    like_str, dislike_str, given_str = sys.argv[1], sys.argv[2], sys.argv[3]

    like_set = set(like_str.split('-'))
    dislike_set = set(dislike_str.split('-'))
    given_list = given_str.split('-')

    happiness = 0

    for num in given_list:
        if num in like_set:
            happiness += 1
        elif num in dislike_set:
            happiness -= 1

    print(happiness)

if __name__ == "__main__":
    calculate_happiness()