#  Q1-> Check if a number is Positive, Negative, or Zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Q2->Check if a number is Odd or Even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q3->Check if two numbers have the same last digit
def lastDigit(a, b):
    return a % 10 == b % 10

print(lastDigit(7, 17))    
print(lastDigit(6, 17))   
print(lastDigit(3, 113))   

# Q4->Print numbers from 1 to 10 in a single row with tab space
for i in range(1, 11):
    print(i, end="\t")
# Q5->Print even numbers between 23 and 57 (each on a new line)
for i in range(23, 58):
    if i % 2 == 0:
        print(i)

# Q6-> Check if a given number is Prime
num = int(input("Enter a number: "))
if num < 2:
    print("Not Prime")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")

#  Q7-> Print prime numbers between 10 and 99
for num in range(10, 100):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num)

# Q8->  Print the sum of all digits of a given number
num = int(input("Enter a number: "))
sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num //= 10
print("Sum of digits:", sum_digits)

# Q9->Reverse a given number
num = int(input("Enter a number: "))
reverse = 0
n = num
while n > 0:
    reverse = reverse * 10 + n % 10
    n //= 10
print("Reversed number:", reverse)

# Q10->Check if a number is a Palindrome
num = int(input("Enter a number: "))
original = num
reverse = 0
while num > 0:
    reverse = reverse * 10 + num % 10
    num //= 10
if original == reverse:
    print(f"{original} is a palindrome.")
else:
    print(f"{original} is not a palindrome.")

