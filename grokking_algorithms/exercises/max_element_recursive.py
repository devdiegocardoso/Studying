# pylint: disable=missing-docstring

def max_recursive(arr,max_element=0):
    if not arr:
        return max_element
    element = arr.pop()
    return max_recursive(arr,max_element=element if element > max_element else max_element)
