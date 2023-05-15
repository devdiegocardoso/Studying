# pylint: disable=missing-docstring

import random as rnd
from timeit import default_timer as timer
from selection_sort import selection_sort
from quick_sort import quick_sort

if __name__ == '__main__':
    test_array = list(range(1,15001))
    rnd.shuffle(test_array)
    print(test_array[:20])
    start = timer()
    result = selection_sort(test_array)
    end = timer()
    print(result[:20])
    print(f"Elapsed time for selection sort: {end-start:.7f} seconds")
    start = timer()
    result = quick_sort(test_array)
    end = timer()
    print(result[:20])
    print(f"Elapsed time for quick sort: {end-start:.7f} seconds")
