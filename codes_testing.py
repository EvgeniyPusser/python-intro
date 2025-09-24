def find_sums(arr, target):
    num_dict = {}
    result = None
    if not arr or len(arr) < 2:
        return None
    for i, num in enumerate(arr):
        complement = target - num
        if complement in num_dict:
            result = (num_dict[complement], i)
            break
        num_dict[num] = i
    
    return result
  
# Example usage:
arr = [2, 7, 11, 15]
target = 26
result = find_sums(arr, target)
print(result)  # Output: (0, 1) because arr[0] + arr[1] = 2 + 7 = 9
# This function finds two numbers in the array that add up to the target sum and returns their

def maxNumberWithOppositeSigns(arr):
    # Convert array to set for O(1) lookup
    num_set = set(arr)
    max_num = None
    max_index = -1
    
    for i, num in enumerate(arr):
        # Check if the opposite sign exists in the array
        if -num in num_set and num != 0:  # Exclude 0 as it doesn't have a meaningful opposite
            # Update max_num if this is the first valid number or has larger absolute value
            # If equal absolute values, prefer the later one (or positive number)
            if max_num is None or abs(num) > abs(max_num) or (abs(num) == abs(max_num) and i > max_index):
                max_num = num
                max_index = i
    
    return (abs(max_num), max_index) if max_num is not None else None

# Example usage:
arr = [3, -1, -4, -90, 90, 2, 4, -3]
result = maxNumberWithOppositeSigns(arr)
print(result)  # Output: (90, 4) because 90 and -90 are in the array and 90 has the largest absolute value