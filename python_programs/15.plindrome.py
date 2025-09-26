# Check if a number is a palindrome

num = int(input("Enter a number: "))

rev = 0
n = abs(num)  # handle negatives (though negative numbers aren't usually palindromes)

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

# restore sign if number was negative
if num < 0:
    rev = -rev

if rev == num:
    print(f"{num} is a Palindrome ✅")
else:
    print(f"{num} is NOT a Palindrome ❌")
