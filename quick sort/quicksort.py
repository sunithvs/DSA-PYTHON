arr = [2, 10,3,4,60,30,6]


def partition(low, high):
    print(low)
    print(high)
    pivot = high
    i = low
    j = high-1
    while True:
        while arr[i] < arr[pivot]:
            i += 1
        print(f"found i = {i}")
        while arr[j] >= arr[pivot]:
            j -= 1
        print(f"found j = {j}")
        if i > j:
            break
        print(f"swappping {arr[i]} and  {arr[j]}")
        arr[i], arr[j] = arr[j], arr[i]

    arr[pivot], arr[i] = arr[i], arr[pivot]
    print(f"array after partition {arr}")

    return i-1


def quick_sort(low,high):
    print(arr[low:high+1])
    if low < high:
        i = partition(low, high)
        print(i)
        quick_sort(low,i)
        quick_sort(i+1,high)
quick_sort(0,len(arr)-1)
print(f"sorted array {arr}")