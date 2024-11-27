def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # 选择中间元素作为基准
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# 测试
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)