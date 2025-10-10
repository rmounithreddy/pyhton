def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  # find the middle index
        
        if arr[mid] == target:
            return mid  # found the element
        elif arr[mid] < target:
            low = mid + 1  # search in the right half
        else:
            high = mid - 1  # search in the left half
            
    return -1  # element not found

nums = list1 = input("Enter first list of numbers separated by spaces: ").split()
target = input("Enter the target number to search for: ")
# Convert inputs to integers
nums = [int(num) for num in nums]
target = int(target)

result = binary_search(nums, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")





#linea search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # return index if found
    return -1  # not found


nums = list1 = input("Enter first list of numbers separated by spaces: ").split()
target = input("Enter the target number to search for: ")
# Convert inputs to integers
nums = [int(num) for num in nums]
target = int(target)


result = binary_search(nums, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
