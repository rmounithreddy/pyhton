#Find the Least Common Multiple (LCM) of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b)
print(f"LCM of {a} and {b} is {lcm(a, b)}")