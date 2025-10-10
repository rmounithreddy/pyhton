#Find factorial using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number to find its factorial: "))
result = factorial(num)
print(f"The factorial of {num} is {result}")

#Find factorial using iterative method
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result   
num = int(input("Enter a number to find its factorial (iterative method): "))
result = factorial_iterative(num)
print(f"The factorial of {num} (iterative method) is {result}")