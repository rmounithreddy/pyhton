#Find the Least Common Multiple (LCM) of two numbers
import math

# Get input from the user
try:
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))

  # Directly use the built-in math.lcm() function
  lcm_value = math.lcm(num1, num2)

  print(f"The LCM of {num1} and {num2} is {lcm_value}")

except ValueError:
  print("Invalid input. Please enter integers only.")