
def permutations(arr: list, index: int):
    if index == len(arr)-1:
        print(arr)
    else:
        for i in range(index, len(arr)):
            # swap
            arr[index], arr[i] = arr[i], arr[index]
            permutations(arr, index+1)
            arr[index], arr[i] = arr[i], arr[index]




arr = list(input("Enter String:").strip())


permutations(arr,0)