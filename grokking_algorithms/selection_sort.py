# pylint: disable=missing-docstring
import operator

def find_smallest(arr):
    key = min(enumerate(arr),key=operator.itemgetter(1))
    return key[0]

def selection_sort(arr):
    new_arr = []
    while len(arr) > 0:
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr
