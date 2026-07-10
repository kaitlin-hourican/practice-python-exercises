import math

def binary_search(nums, target):
    search_list = nums

    while len(search_list) > 0:
        middle_index = len(search_list) // 2 
        middle_num = search_list[middle_index]

        print(middle_num, ":", search_list)

        if middle_num < target:
            search_list = search_list[middle_index + 1:]
        elif middle_num > target:
            search_list = search_list[:middle_index]
        else:
            return True
    
    return False

def binary_search_pointers(nums, target):
    start_index = 0
    end_index = len(nums) - 1

    while start_index <= end_index:
        middle_index = (start_index + end_index) // 2 
        middle_num = nums[middle_index]

        if middle_num < target:
            start_index = middle_index + 1
        elif middle_num > target:
            end_index = middle_index - 1
        else:
            return True
    
    return False

print(binary_search_pointers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 1))
print(binary_search_pointers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15))
print(binary_search_pointers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 2))
print(binary_search_pointers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 4))
print(binary_search_pointers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 13))
print(binary_search_pointers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], -1))
print(binary_search_pointers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 16))
