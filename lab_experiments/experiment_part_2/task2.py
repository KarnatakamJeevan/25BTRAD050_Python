# Lab Exercise 6: Prime number and factorial
programs
# Part A: Check whether a number is prime
def is_prime(n):
if n < 2:
return False
for i in range(2, int(n ** 0.5) + 1):
if n % i == 0:
return False
return True
num = int(input("Enter a number to check if
it is prime: "))
if is_prime(num):
print(f"{num} is a Prime number.")
else:
print(f"{num} is not a Prime number.")
# Part B: Calculate factorial of a number
def factorial(n):
result = 1
for i in range(1, n + 1):
result *= i
return result
num2 = int(input("Enter a number to find its
factorial: "))
print(f"Factorial of {num2} is
{factorial(num2)}.")Output:
