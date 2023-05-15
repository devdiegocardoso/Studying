# pylint: disable=missing-docstring
def binary_search(arr,item):
    low = 0
    high = len(arr) - 1
    return binary_search_recursive(arr,item,low,high)

def binary_search_recursive(arr,item,low,high):
    if low > high:
        return None
    mid = (low + high) // 2
    if item == arr[mid]:
        return mid
    if item > arr[mid]:
        return binary_search_recursive(arr,item,mid+1,high)
    return binary_search_recursive(arr,item,low,mid-1)
