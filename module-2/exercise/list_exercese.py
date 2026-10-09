# Given a list of integers, iterate through the items and count how many are even and how many are odd.
# num = [10, 21, 4, 45, 66, 93, 11]
# print(f'Even: {len(list(filter(lambda x: x%2 == 0, num)))}')
# print(f'Odd: {len(list(filter(lambda x: x%2 != 0, num)))}')
# *******************************************************************************************************************

# Given a list, extract a “slice” containing the middle three elements.
# lst = [10, 20, 30, 40, 50, 60, 70]
# middle_index = len(lst) // 2
# print(lst[middle_index-1:middle_index+2])
# *******************************************************************************************************************

# Write a script to swap the positions of two elements in a list based on their indices.
# Indices to Swap: 0 and 2
# indx1, indx2 = 0, 2
#
# Lst2 = [23, 65, 19, 90]
#
# Lst2[indx1], Lst2[indx2] = Lst2[indx2], Lst2[indx1]
# print(Lst2)
# *******************************************************************************************************************
#  In a list of strings, identify which string has the most characters.
# words = ["PHP", "Exercises", "Backend", "Python"]
# longest = max(words, key=len)
# print(longest)

# *******************************************************************************************************************
#  Find out how many times a specific value appears in a list.
# lst3 = [10, 20, 30, 10, 40, 10, 50]
# print(lst3.count(10))

# *******************************************************************************************************************
# data = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# clean_data = [name for name in data if name != ""]
# print(clean_data)
# *******************************************************************************************************************
# Given two lists of strings, combine them index-by-index to form a single list of concatenated strings.
# List1 =  ["Py", "is", "awes"]
# List2 = ["thon", " ", "ome"]
# concatenated = [x+y for x,y in zip(List1, List2)]
# print(concatenated)

# *******************************************************************************************************************
# Find a specific item in a list and insert a new item immediately after it.
# list4 = [10, 20, 30, 40, 50]
#
# # insert 100 after 30
# target = list4.index(30) +1
# print(target)
# list4.insert(target, 100)
# print(list4)
# *******************************************************************************************************************
# frequency = {}
# arr = [1, 3, 3, 2, 1, 1, 4, 3, 3]


# Count occurrences of each element
# for item in arr:
#     frequency[item] = frequency.get(item, 0) + 1
# print(frequency)

# *******************************************************************************************************************
# Given three separate lists, write a function that returns a list containing only the elements that appear in all three.
# lista = [1, 5, 10, 20]
# listb = [6, 7, 20, 80, 100]
# listc = [3, 4, 15, 20, 30, 70, 80]
#
# def common_elements(ls1, ls2, ls3):
#     common = set(ls1) & set(ls2) & set(ls3)
#     return list(common)
#
# result = common_elements(lista, listb, listc)
# print(result)

# *******************************************************************************************************************
# Write a function that takes a list of strings and an integer k. The function should return a new list containing only
# the strings that have a length greater than or equal to k.
# def filter_elements(arr, length):
#     return list(filter(lambda x: len(x) >= length, arr))
#
# filtered = filter_elements(["apple", "pie", "banana", "kiwi", "pear"], 5)
# print(filtered)

# *******************************************************************************************************************
# Create a function that determines if a list of numbers is sorted in non-decreasing (ascending) order.
# Return True if it is, and False otherwise.

# def check_order(lst):
#     return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
#
# print(check_order([10, 20, 25, 30, 40]))

# *******************************************************************************************************************
# Given two lists of the same length, one containing keys and the other containing values.
# combine them into a single dictionary.
# keys = ["name", "age", "city"]
# values = ["Alice", 25, "New York"]
#
# dictionary = {key: value for key, value in zip(keys,values)}
# print(dictionary)

# *******************************************************************************************************************
# Create a function that transforms a list of numbers into their cumulative sum.
# Each element at index i in the new list should be the sum of all elements from index 0 to i in the original list.

# lst5 = [10, 20, 30, 40]
# prefix_sum = []
# result = 0
# for item in lst5:
#     result += item
#     prefix_sum.append(result)
# print(prefix_sum)
# *******************************************************************************************************************

# def split_chunks(lst, n):
#     """Yield successive n-sized chunks from lst."""
#     splitted = []
#     for i in range(0, len(lst), n):
#         splitted. append(lst[i:i + n])
#     return splitted
#
# print(split_chunks([1, 2, 3, 4, 5], 2))

# *******************************************************************************************************************
# def splitted(lst, n):
#     splitted = []
#     for i in range(0, len(lst), n):
#         print(lst[i: i+n])
#
# splitted([1, 2, 3, 4, 5], 2)
# *******************************************************************************************************************
# Given a list of numbers, push all zeros to the end of the list while maintaining the relative order of all
# non-zero elements. This must be done efficiently.

def shift_zeros(lst):
    for item in lst:
        if item == 0:
            lst.remove(item)
            lst.append(item)
    return lst

print(shift_zeros([0, 1, 0, 3, 12]))


# *******************************************************************************************************************
# *******************************************************************************************************************
# *******************************************************************************************************************