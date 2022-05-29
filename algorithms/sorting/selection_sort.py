# Selection sort involves finding the minimum element in one pass through the array
# and then swapping it with the first position of the unsorted part of the array.
# Time complexity of selection sort is O(n^2) in all cases

def selection_sort(array):
    for i in range(len(array)):
        min = array[i]
        minimum_index = i
        for j in range(i+1, len(array)):
            if array[j] < min:
                min = array[j]
                minimum_index = j
        if minimum_index != i:  # If minimum index has changed, i.e, a smaller  element has been found, then we swap that element with the ith element
            array[minimum_index], array[i] = array[i], array[minimum_index]
    return array


array = [5, 9, 3, 10, 45, 2, 0]
print(selection_sort(array))
