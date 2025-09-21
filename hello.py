import bisect

def bSearchSortedList(arr, target):
    idx = bisect.bisect_left(arr, target)
    if idx < len(arr) and arr[idx] == target:
        return idx
    else:
        return -(idx + 1)

arr = [1, 1, 1, 3, 4, 5, 11]

print(bSearchSortedList(arr, 3))
print(bSearchSortedList(arr, 6))
print(bSearchSortedList(arr, 1))
print(bSearchSortedList(arr, 0))
print(bSearchSortedList(arr, 2))
