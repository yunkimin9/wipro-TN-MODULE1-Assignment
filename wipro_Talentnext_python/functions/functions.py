

# Q1: Sum of all numbers in a list
def sum_list(numbers):
    return sum(numbers)

# Q2: Reverse a string
def reverse_string(s):
    return s[::-1]

# Q3: Factorial of a non-negative number
def factorial(n):
    if n < 0:
        return "Invalid input"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Q4: Count upper and lower case letters in a string
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print("Upper case letters:", upper)
    print("Lower case letters:", lower)

# Q5: Return even numbers from a list
def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# Q6: Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    print("Sum of list:", sum_list([8, 2, 3, 0, 7]))               
    print("Reversed string:", reverse_string("1234abcd"))          
    print("Factorial of 5:", factorial(5))                         
    count_case("Hello World! Python123")                           
    print("Even numbers:", get_even_numbers([1,2,3,4,5,6,7,8,9]))   
    print("Is 17 prime?", is_prime(17))                            
    print("Is 18 prime?", is_prime(18))                          