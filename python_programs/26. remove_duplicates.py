#Remove duplicates from a list

numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
unique_numbers = list(set(numbers))
print("List after removing duplicates:", unique_numbers)

#Merge two lists and sort them
list1 = input("Enter first list of numbers separated by spaces: ").split()
list1 = [int(num) for num in list1]
list2 = input("Enter second list of numbers separated by spaces: ").split()
list2 = [int(num) for num in list2]
merged_list = list1 + list2
sorted_list = sorted(merged_list)   
print("Merged and sorted list:", sorted_list)