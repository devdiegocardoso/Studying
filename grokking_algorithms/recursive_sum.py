# pylint: disable=missing-docstring

def recursive_sum(arr,index):
    return 0 if index == -1 else arr[index] + recursive_sum(arr,index-1)

numbers_1 = [1,2,3]
numbers_2 = [2,4,6,8,10]
numbers_3 = [-2,-4,-6]
numbers_4 = []

print(recursive_sum(numbers_1,len(numbers_1)-1))
print(recursive_sum(numbers_2,len(numbers_2)-1))
print(recursive_sum(numbers_3,len(numbers_3)-1))
print(recursive_sum(numbers_4,len(numbers_4)-1))
