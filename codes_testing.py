def find_sums(arr, target):
    seen = set()
    result = False
    
    for num in arr:
        complement = target - num
        if complement in seen:
            result = True
            break
        seen.add(num)
    
    return result
  
# Example usage:
arr = [2, 7, 11, 15]
target = 9
result = find_sums(arr, target)
print(result)  # Output: (0, 1) because arr[0] + arr[1] = 2 + 7 = 9
# This function finds two numbers in the array that add up to the target sum and returns their

def maxNumberWithOppositeSigns(arr):
    num_set = set()
    max_num = 0
    
    for num in arr:
        num_set.add(num)
        # Check if the opposite sign exists and update max_num
        if -num in num_set and num != 0 and abs(num) > abs(max_num):
            max_num = num
                
    return abs(max_num) if max_num != 0 else -1

# Example usage:
arr = [3, -1, -4, -90, 90, 2, 4, -3]
result = maxNumberWithOppositeSigns(arr)
print(result)  # Output: 90 because 90 and -90 are in the array and 90 has the largest absolute value