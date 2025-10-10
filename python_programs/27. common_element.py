#Find common elements between two lists
list1 = input("Enter first list of numbers separated by spaces: ").split()
list1 = [int(num) for num in list1]
list2 = input("Enter second list of numbers separated by spaces: ").split()
list2 = [int(num) for num in list2]
common_elements = list(set(list1) & set(list2))
print("Common elements:", common_elements)