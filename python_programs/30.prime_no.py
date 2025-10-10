lst = [2, 3, 4, 5, 6, 7, 8, 9, 10]

primes = []
for n in lst:
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                break
        else:
            primes.append(n)

print("Prime numbers:", primes)
