#Remove all vowels from a string
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
new_string = ''.join([char for char in string if char not in vowels])
print("String after removing vowels:", new_string)



#Example
# Input: "Hello World"
# Output: "Hll Wrld"