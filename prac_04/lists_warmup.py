numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[0])  # 3
print(numbers[-1]) # 2
print(numbers[3])  # 1
print(numbers[:-1]) # [3, 1, 4, 1, 5, 9]
print(numbers[3:4]) # [1]
print(5 in numbers) # True
print(7 in numbers) # False
print("3" in numbers) # False, because "3" is a string and the list contains integers
print(numbers + [6, 5, 3]) # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# Change the first and last elements in the list
numbers[0] = "ten"  # Change first element to 'ten'
numbers[-1] = 1     # Change last element to
# Change the first and last elements in the list
numbers[0] = "ten"  # Change first element to 'ten'
numbers[-1] = 1     # Change last element to 1
# Print list elements excluding the first two and check membership of 9
print(numbers[2:])  # Print all elements from index 2 to the end
print(9 in numbers) # Check if 9 is in the list
