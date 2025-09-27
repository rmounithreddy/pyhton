#check whether a number is prime or not
num = int(input())

for i in range(2,num):
    if num % i ==0:
        print("no")
        break
else:
    print("yes")


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