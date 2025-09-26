#check whether a number is prime or not
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not prime")
            break
    else:
        print(f"{num} is prime")
else:
    print(f"{num} is not prime")

# Print all prime numbers between 1 and 100
for num in range(2, 101):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")


#sum of first n natural numbers from 1 to n
n = int(input("Enter n: "))
total = n * (n + 1) // 2   # Formula for sum of first n natural numbers
print(f"Sum = {total}")