#Count frequency of each character in a string
string = input("Enter a string: ")
frequency = {}
for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print("Character frequency:")
for char, freq in frequency.items():
    print(f"'{char}': {freq}")
    