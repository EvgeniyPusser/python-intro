def bSearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1       

if __name__ == "__main__":
    arr = [1, 2, 2, 2, 5, 6, 7, 8, 9]
    target = 2
    result = bSearch(arr, target)
    print(f"Element found at index: {result}" if result != -1 else "Element not found")     



