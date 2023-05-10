# pylint: disable=missing-docstring

def recursive_count(arr):
    if not arr:
        return 0
    arr.pop()
    return 1 + recursive_count(arr)
