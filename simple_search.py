# pylint: disable=missing-docstring

def simple_search(arr,item):
    for index,element in enumerate(arr):
        if item == element:
            return index
    return None
