def binary_search(arr: list, ele: int):
    l = len(arr)

    if l >= 1:
        left = 0
        right = l - 1
        mid = int((left + right) / 2)
        mid_ele = arr[mid]

        if ele == mid_ele:
            print('found')
        elif ele < mid_ele:
            binary_search(arr[:mid], ele)
        elif ele > mid_ele:
            binary_search(arr[mid+1:], ele)
    else:
        print('not found')


if __name__ == '__main__':
    arr = list(map(int, input('Enter space separated number : ').strip().split()))
    ele = int(input('What to search : '))
    # binary search needs sorted array
    arr.sort()

    binary_search(arr, ele)
