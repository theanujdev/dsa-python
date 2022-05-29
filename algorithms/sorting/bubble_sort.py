# In Bubble Sort, the largest value is bubbled up in every pass.
# Every two adjacent items are compared and they are swapped if they are in the wrong order.
# This way, after every pass, the largest element reaches to the end of the array.
# Time complexity of Bubble Sort in Worst and Average Case is O(n^2) and in best case, its O(n)

def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


array = [5, 9, 3, 10, 45, 2, 0]
print(bubble_sort(array))
