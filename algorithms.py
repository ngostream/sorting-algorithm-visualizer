# algorithms.py

def bubble_sort(array, visualize):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                visualize(array)

def merge_sort(array, visualize):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left, visualize)
        merge_sort(right, visualize)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
            visualize(array)
        
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
            visualize(array)
        
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
            visualize(array)
