# pylint: disable=missing-docstring

from timeit import default_timer as timer
from binary_search import binary_search
from simple_search import simple_search

if __name__ == '__main__':
    test_array = list(range(1,100000001))
    start = timer()
    result = simple_search(test_array,100000000)
    end = timer()
    print(f"Elapsed time for simple search: {end-start:.7f} seconds")
    start = timer()
    result = binary_search(test_array,100000000)
    end = timer()
    print(f"Elapsed time for binary search: {end-start:.7f} seconds")
