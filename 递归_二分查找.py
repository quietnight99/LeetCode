def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # 目标元素不存在


    mid = (left + right) // 2
    if arr[mid] == target:
        return mid  # 找到目标元素，返回索引
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)  # 在右半部分继续查找
    else:
        return binary_search_recursive(arr, target, left, mid - 1)  # 在左半部分继续查找


# 示例用法
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
if result != -1:
    print(f"目标元素 {target} 在数组中的索引为 {result}")
else:
    print(f"数组中不存在目标元素 {target}")