lst = [6, 7, 3, 0, 4, 8, 15, 4]


# 冒泡排序算法
def bubbleSort(arr):
    sum = len(arr)
    for i in range(sum - 1):
        for j in range(sum - i - 1):
            if arr[j] < arr[j + 1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp


# 插入排序算法
def insertionSort(arr):
    sum = len(arr)
    for i in range(1, sum):
        j = i
        target = arr[i]
        while j > 0 and target < arr[j - 1]:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = target


# 选择排序算法
def selectionSort(arr):
    sum = len(arr)
    for i in range(sum):
        max = i
        for j in range(i, sum):
            if arr[j] > arr[max]:
                max = j
        temp = arr[i]
        arr[i] = arr[max]
        arr[max] = temp


# 快速排序算法
def quickSort(aar, low, heigh):
    if low < heigh:
        index = getPivot(aar, low, heigh)
        quickSort(aar, 0, index - 1)
        quickSort(aar, index + 1, heigh)


def getPivot(aar, low, heigh):
    # 基准数据为数组第一个元素
    pivot = aar[low]
    while low < heigh:
        # 当队尾的元素大于等于基准数据时，向前挪动heigh的指针
        while low < heigh and aar[heigh] >= pivot:
            heigh = heigh - 1

        # 如果队尾元素小于tmp了，需要将其赋值给low
        aar[low] = aar[heigh]

        # 当队首元素小于等于pivot时，向前挪动low指针
        while low < heigh and aar[low] <= pivot:
            low = low + 1

        # 当队首元素大于pivot时，需要将其赋值给high
        aar[heigh] = aar[low]

    # 跳出循环时low和high相等，此时的low或high就是pivot的正确索引位置
    aar[low] = pivot

    return low


# 快速排序，比上一个快速排序方法更容易理解
def quickSort2(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quickSort2(less) + [pivot] + quickSort2(greater)


# 测试代码
bubbleSort(lst)
print("bubble sort:")
print(lst)
print('\n')
insertionSort(lst)
print("insertion sort:")
print(lst)
print('\n')
selectionSort(lst)
print("selection sort:")
print(lst)
print('\n')
quickSort(lst, 0, len(lst) - 1)
print("quick sort:")
print(lst)
print('\n')

# 测试快速排序
lst = [6, 7, 3, 0, 4, 8, 15, 4]
lst = quickSort2(lst)
print("quick sort 2:")
print(lst)
print('\n')
