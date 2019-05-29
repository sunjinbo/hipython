lst = [0, 7, 9, 10, 14, 18, 25, 41, 53]


# 顺序查找算法
# 时间复杂度O(n)
# 最基础的遍历无序列表的查找算法
def sequentialSearch(lst, key):
    length = len(lst)
    for i in range(length):
        if lst[i] == key:
            return i
    return -1


# 二分查找算法
# 时间复杂度为 O(logn) 
# 针对有序查找表的二分查找算法
def binarySearch(lst, key, low, high):
    mid = int((high - low) / 2 + low)
    if low <= high:
        if lst[mid] > key:
            return binarySearch(lst, key, low, mid - 1)
        elif lst[mid] < key:
            return binarySearch(lst, key, mid + 1, high)
        else:
            return mid
    else:
        return -1


# 插值查找算法
# 如果元素均匀分布，则O（log log n）），在最坏的情况下可能需要 O（n）
# 关键字分布又比较均匀查找比较有优势
# 基于二分查找算法，将查找点的选择改进为自适应选择，可以提高查找效率。当然，差值查找也属于有序查找。
def interpolationSearch(lst, key, low, high):
    mid = int((high - low) * ((key - lst[low]) / (lst[high] - lst[low])) + low)
    if low <= high:
        if lst[mid] > key:
            return interpolationSearch(lst, key, low, mid - 1)
        elif lst[mid] < key:
            return interpolationSearch(lst, key, mid + 1, high)
        else:
            return mid
    else:
        return -1


pos = sequentialSearch(lst, 10)
print("sequential search:" + str(pos))
pos = binarySearch(lst, 14, 0, len(lst) - 1)
print("binary search:" + str(pos))
pos = interpolationSearch(lst, 18, 0, len(lst) - 1)
print("interpolation search:" + str(pos))
