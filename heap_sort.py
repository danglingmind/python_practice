def max_heapify(arr: list, i: int, n: int):
    left = 2*i
    right = 2*i+1
    if left <= n and arr[left] > arr[i]:
        largest = left
    else:
        largest = i

    if right <= n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[largest] , arr[i] = arr[i] , arr[largest]
        max_heapify(arr, largest, n)

def build_max_heap(arr: list):
    n = len(arr)-1
    for i in range(n//2 , 0, -1):
        max_heapify(arr, i, n)

def heap_sort(arr: list):
    arr.insert(0, -1) # convert the array index to start from 1 for easy calculations
    build_max_heap(arr)
    print(arr)
    l = len(arr)-1
    for i in range(l, 0, -1):
        arr[i], arr[1] = arr[1], arr[i]
        max_heapify(arr, 1, i-1)

arr = list(map(int, input('Space separateed numbers:').strip().split()))



# now to sort just pop the top element as it

heap_sort(arr)

print(arr[1:])