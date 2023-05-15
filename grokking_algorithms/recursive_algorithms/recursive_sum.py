# pylint: disable=missing-docstring

def recursive_sum(arr,index):
    return 0 if index == -1 else arr[index] + recursive_sum(arr,index-1)

numbers_1 = [1,2,3]
numbers_2 = [2,4,6,8,10]
numbers_3 = [-2,-4,-6]
numbers_4 = []
