# pylint: disable=missing-docstring
#import operator

""" def find_smallest(arr):
    key = min(enumerate(arr),key=operator.itemgetter(1))
    return key[0]

def selection_sort(arr):
    new_arr = []
    while len(arr) > 0:
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr """

def selection_sort(arr):
    arr_copy = arr.copy()
    for i,_ in enumerate(arr_copy):
        min_index = i
        for j in range(i+1,len(arr_copy)):
            if arr_copy[min_index] > arr_copy[j]:
                min_index = j
        arr_copy[i] , arr_copy[min_index] = arr_copy[min_index] , arr_copy[i]
    return arr_copy
