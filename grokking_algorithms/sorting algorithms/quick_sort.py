# pylint: disable=missing-docstring
from random import randint

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot_index = randint(0,len(arr)-1)
    pivot = arr[pivot_index]
    less = [n for n in arr[:pivot_index]+arr[pivot_index+1:] if n <= pivot]
    greater = [n for n in arr[:pivot_index]+arr[pivot_index+1:] if n > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)
