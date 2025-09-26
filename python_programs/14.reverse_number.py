# Program to reverse a number
num=int(input("Enter a number: "))
rev=0
num=abs(num)  # Handle negative numbers

while(num>0):
    digit=num%10 # Extract the last digit
    rev=rev*10+digit # Append it to the reversed number
    num=num//10 # Remove the last digit from the original number

print("Reversed Number: ",rev)


