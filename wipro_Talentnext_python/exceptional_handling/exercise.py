 # Q1: Division with exception handling
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numeric values.")
except Exception as e:
    print(f"Unexpected error: {e}")

print("\n" + "-"*50 + "\n")

# Q2: Check prime number with input validation
try:
    num = int(input("Enter a number to check if it's prime: "))
    if num < 2:
        print("Not a prime number.")
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print("Not a prime number.")
                break
        else:
            print("It is a prime number.")
except ValueError:
    print("Error: You must enter a valid integer.")

print("\n" + "-"*50 + "\n")

# Q3: Read file and display in title case
filename = input("Enter the filename to open (with .txt): ")
try:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print("File content in Title Case:\n")
        print(content.title())
except FileNotFoundError:
    print("Error: File not found. Please check the file name.")
except Exception as e:
    print(f"Unexpected error: {e}")

print("\n" + "-"*50 + "\n")

# Q4: Index access with error handling
numbers = [10, -5, 3, 0, -8, 22, -11, 9, 17, -2]
try:
    index = int(input("Enter an index (0–9): "))
    value = numbers[index]
    if value >= 0:
        print(f"The number at index {index} is Positive.")
    else:
        print(f"The number at index {index} is Negative.")
except IndexError:
    print("Error: Index out of range. Please enter a number between 0 and 9.")
except ValueError:
    print("Error: Please enter a valid integer.")