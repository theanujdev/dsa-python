def binarySearch(array, target):
    low = 0
    high = len(array) - 1
    # Repeat until the pointers low and high meet each other
    while low <= high:
        mid = (low + high)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binarySearchRecursive(array, target, low, high):
    if high >= low:
        mid = low + (high - low)//2
        # If found at mid, then return it
        if array[mid] == target:
            return mid
        # Search the left half
        elif array[mid] > target:
            return binarySearchRecursive(array, target, low, mid-1)
        # Search the right half
        else:
            return binarySearchRecursive(array, target, mid + 1, high)
    else:
        return -1


array = [3, 4, 5, 6, 7, 8, 9]
target = 4

result = binarySearch(array, target)
print(result)
