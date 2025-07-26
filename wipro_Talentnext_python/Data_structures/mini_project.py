''' project-1
Q-> Create a dictionary that contains a list of people and one interesting fact about each of the.
display each person and his or her intresting fact to the screen. next, change a fact about one of 
the people. alos add an additional person and corresponding fact. display the new list of people
and facts. run the program multiple times and notice if the order changes.
'''
# mini_project.py

def display_facts(facts):
    for person, fact in facts.items():
        print(f"{person}: {fact}")

def main():
    # Initial dictionary of people and their interesting facts
    people_facts = {
        "Jeff": "Is afraid of Dogs.",
        "David": "Plays the piano.",
        "Jason": "Can fly an airplane."
    }

    print("Original facts:")
    display_facts(people_facts)

    print("\nUpdated facts:")
    # Change Jeff's fact
    people_facts["Jeff"] = "Is afraid of heights."
    # Add a new person
    people_facts["Jill"] = "Can hula dance."

    display_facts(people_facts)

if __name__ == "__main__":
    main()
''' Project-2
Q-> Given the participant's score sheet for your university sports day, you are required to find
the runner-up score. you have scores store them in a list and find the score of the runner-up.

'''
# mini_project2.py

def find_runner_up(scores):
    # Remove duplicates by converting to set
    unique_scores = list(set(scores))

    # Sort in descending order
    unique_scores.sort(reverse=True)

    # Check if we have at least 2 unique scores
    if len(unique_scores) < 2:
        return "Runner-up score not found. Not enough unique scores."
    
    # Return the second highest score
    return unique_scores[1]

def main():
    # You can take input from user or hardcode like this
    scores = [2, 3, 6, 6, 5]

    runner_up = find_runner_up(scores)
    print("Runner-up score:", runner_up)

if __name__ == "__main__":
    main()


''' Project-3
Q-> you have a record of n students. each record contains the student's name,and their percent marks in 
math,physics and chemistry . the marks can be floating values. you are required to save the record
in a dictionary data types.
student's name is the key. marks stored in a list is the value. the user enters a student's name.
output the average percentage marks obtained by that student.
'''


def calculate_average(student_data, name):
    if name in student_data:
        marks = student_data[name]
        average = sum(marks) / len(marks)
        return average
    else:
        return None

def main():
    
    students = {
        "Krishna": [67, 68, 69],
        "Arjun": [70, 98, 63],
        "Malika": [52, 56, 60]
    }

    
    name = input("Enter a name: ")

    avg = calculate_average(students, name)

    if avg is not None:
        print(f"Average percentage mark: {int(avg)}")
    else:
        print("Student not found.")

if __name__ == "__main__":
    main()


''' Project-4
Q-> Given a string of n words, help alex to find out how many times his name appears in the string



'''


def count_name_occurrences(text, name="Alex"):
    return text.count(name)

def main():
   
    text = input("Enter the string: ")

    
    if 1 <= len(text.split()) <= 200:
        count = count_name_occurrences(text, "Alex")
        print(f"{count}")
    else:
        print("Input does not meet the word count constraint (1 <= n <= 200).")

if __name__ == "__main__":
    main()
