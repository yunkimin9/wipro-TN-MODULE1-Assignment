
import re
from collections import Counter

def get_meeting_time(line_count):
    if line_count <= 12:
        return f"{line_count} AM"
    else:
        hour = line_count - 12
        return f"{hour} PM"

def get_meeting_place(text):
    words = re.findall(r'\b\w+\b', text.lower())

    word_counts = Counter(words)

    most_common_word, _ = word_counts.most_common(1)[0]

    return f"{most_common_word.capitalize()} Street"

def main():
    file_path = "sample.txt"  

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            text = file.read() 

        full_text = ' '.join(lines)
        num_lines = len(lines)
        meeting_time = get_meeting_time(num_lines)
        meeting_place = get_meeting_place(full_text)
        print(f"Meeting time: {meeting_time}")
        print(f"Meeting place: {meeting_place}")

    except FileNotFoundError:
        print(f"File '{file_path}' not found. Please check the path and try again.")

if __name__ == "__main__":
    main()