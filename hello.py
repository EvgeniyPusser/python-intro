# x: int = 1
# x=2
# print(x)
# y = "hello"
def bSearchSortedList(arr, target):
    # найдём левую границу: первый индекс, где arr[idx] >= target
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1

    
    return left if left < len(arr) and arr[left] == target else -(left + 1)

      
      # не найдено → код вставки
arr = [1, 1, 1, 3, 4, 5, 11]

print(bSearchSortedList(arr, 3))
print(bSearchSortedList(arr, 6))
print(bSearchSortedList(arr, 1))
print(bSearchSortedList(arr, 0))
print(bSearchSortedList(arr, 2))
