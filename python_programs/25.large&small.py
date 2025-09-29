#Find the largest and smallest number in a list

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
largest = max(numbers)
smallest = min(numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)

#Find the second largest number in a list
unique_numbers = set(numbers)

# Check if there are at least two unique numbers
if len(unique_numbers) < 2:
    print("Not enough unique numbers to determine the second largest.")
else:
    unique_numbers.remove(largest)
    second_largest = max(unique_numbers)
    print("Second largest number:", second_largest)