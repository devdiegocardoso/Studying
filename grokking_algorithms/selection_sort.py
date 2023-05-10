# pylint: disable=missing-docstring

def selection_sort(arr):
    arr_copy = arr.copy()
    for i,_ in enumerate(arr_copy):
        min_index = i
        for j in range(i+1,len(arr_copy)):
            if arr_copy[min_index] > arr_copy[j]:
                min_index = j
        arr_copy[i] , arr_copy[min_index] = arr_copy[min_index] , arr_copy[i]
    return arr_copy
