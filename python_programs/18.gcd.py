#Find the Greatest Common Divisor (GCD) of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(f"GCD of {a} and {b} is {gcd(a, b)}")
