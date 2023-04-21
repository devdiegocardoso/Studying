# pylint: disable=missing-docstring

def simple_search(arr,item):
    return next(
        (index for index, element in enumerate(arr) if item == element), None
    )
