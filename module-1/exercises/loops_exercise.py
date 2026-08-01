# Write a program to display numbers from -10 to -1 using a for loop.
# for i in range(-10,0):
#     print(i)

#---------------------------------------------------------------------------------------------------
# Write a program to display a message “Done” after the successful execution of a for loop that iterates from 0 to 4.
# for i in range(5):
#     print(i)
#     if i==4:
#         print('Done!')
#---------------------------------------------------------------------------------------------------
# Write a program that accepts a number from the user and calculates the sum of all numbers from 1 up to that number.

# number = int(input('Enter a number: '))
# sum = 0
# for i in range(number+1):
#     sum += i
# print(sum)
#---------------------------------------------------------------------------------------------------
# Write a program that takes an integer n and prints the cube of every number from 1 to n in the
# format Current Number is : 1 and the cube is 1.
# try:
#     number = int(input('Enter a number: '))
#     for num in range(number):
#         print(f'The current number is: {num} and cube is {num ** 3}')
# except (ValueError, TypeError) as e:
#     print(f'{e}: You did not enter a number.')
#
# print('Done!')
#---------------------------------------------------------------------------------------------------
# Given a list of numbers, use a loop to count how many times a specific number (e.g., 10) appears.
# list1 = [10, 20, 10, 30, 10, 40, 50]
# target = 10
# occurrence = 0
# for num in list1:
#     if num == target:
#         occurrence += 1
# print(f'{target} occurs {occurrence} times.')

#---------------------------------------------------------------------------------------------------
# Given a Python list, use a loop to print only the elements that are located at odd
# index positions (index 1, 3, 5, etc.).
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# odd_indexes = [value for index, value in enumerate(my_list) if index % 2 != 0]
# print(odd_indexes)
# **********************************************
# odd_indexes = []
# for index, value in enumerate(my_list):
#     if index % 2 != 0:
#         odd_indexes.append(value)
# print(odd_indexes)

#---------------------------------------------------------------------------------------------------
# Given a list, iterate it in reverse order and print each element.
# list1 = [10, 20, 30, 40, 50]
# for item in list1[::-1]:
#     print(item)
# for item in reversed(list1):
#     print(item)

#---------------------------------------------------------------------------------------------------
# Write a program that takes a string and reverses it using a for loop. While Python’s [::-1] shortcut is famous,
# reversing a string manually is a classic way to understand how sequences are constructed.
# str1 = "Python"
# reversed_str1 = ''
# for i in range(len(str1)):
#     reversed_str1 += str1[-(i+1)]
# print(reversed_str1)
#---------------------------------------------------------------------------------------------------
# Write a program that counts the total number of vowels and consonants in a given sentence, ignoring spaces and
# special characters.
# given = "Loops are Fun!"
# vowels = ['a', 'e', 'i', 'o', 'u']
# vowel_count = 0
# consonant_count = 0
#
# for char in given:
#     if char.isalpha():
#         if char in vowels:
#             vowel_count += 1
#         else:
#             consonant_count += 1
# print(f'Vowels: {vowel_count} and Consonants: {consonant_count}')

#---------------------------------------------------------------------------------------------------
# Write a program to find the largest and smallest digit within a given integer (e.g., in 75869, the largest is
# 9 and the smallest is 5).
# num = 75869
# Initialize with opposite extremes
# largest = 0
# smallest = 9
#
# while num > 0:
#     digit = num % 10
#
#     # Check for new largest
#     if digit > largest:
#         largest = digit
#     # Check for new smallest
#     if digit < smallest:
#         smallest = digit
#
#     num = num // 10
#
# print("Largest digit:", largest)
# print("Smallest digit:", smallest)

# print(7586 % 10)
#---------------------------------------------------------------------------------------------------
# Write a program to use a loop to find the factorial of a given number (e.g., 5!).
# The factorial of N is the product of all integers from 1 to N.

# def num_factorial(n):
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial *=i
#     return factorial
#
# print(num_factorial(5))
#---------------------------------------------------------------------------------------------------
# Write a program to check if a number is an Armstrong number. An Armstrong number (for a 3-digit number)
# is an integer such that the sum of the cubes of its digits is equal to the number itself (e.g., 153 = 1^3 + 5^3 + 3^3).
# def check_armstrong(num):
#     cube = 0
#     if isinstance(num, int):
#         numlist = list(str(num))
#         for item in numlist:
#             cube += int(item) **3
#     return True if cube == num else False
#
# print(check_armstrong(153))
#---------------------------------------------------------------------------------------------------
# Write a program to print a right-angled triangle pattern where each row contains increasing numbers up to the row number.
# for i in range(1,6):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print("")

#---------------------------------------------------------------------------------------------------
# Write a program to use for loop to print the following reverse number pattern:
# for i in range(0,5):
#     for j in reversed(range(1,6)):
#         if j-i > 0:
#             print(j-i, end=" ")
#     print("")

#---------------------------------------------------------------------------------------------------
# Print a 5*5 square of stars where the middle is empty, leaving only the border.
# for i in range(5):
#     if i in [1, 2, 3]:
#         print(f'* {' ' * 3}   *')
#     else:
#         print("* "*5)

#---------------------------------------------------------------------------------------------------
# Given a list of numbers, create a new list where each element is the sum of all elements from the original
# list up to that position.
# given = [1, 2, 3, 4]
# cumulative = []
# current_sum = 0
# for num in given:
#     current_sum += num
#     cumulative.append(current_sum)
#
# print(cumulative)

#---------------------------------------------------------------------------------------------------
#  Given a dictionary of student scores, create a new dictionary that only includes students who scored
#  above a certain threshold (e.g., 75).
# scores = {"Alice": 85, "Bob": 70, "Charlie": 95, "David": 60}
# high_scorers = {}
# threshold = 75
# for student, score in scores.items():
#     if score >= threshold:
#         high_scorers[student] = score
#
# print(high_scorers)
#---------------------------------------------------------------------------------------------------
# Given two lists, find the elements that appear in both. Do not use Python’s built-in set().intersection() method.
# list_a = [1, 2, 3, 4, 5]
# list_b = [4, 5, 6, 7, 8]
# common_elements = []
# for element in list_a:
#     if element in list_b:
#         common_elements.append(element)
# print(common_elements)
#---------------------------------------------------------------------------------------------------
# Write a program to remove all duplicate values from a list using a loop, maintaining the original order of elements.
# given = [1, 2, 2, 3, 4, 4, 4, 5]
# seen = []
# for num in given:
#     if num not in seen:
#         seen.append(num)
# print(seen)
#---------------------------------------------------------------------------------------------------
# Given a list of integers, move all even numbers to the beginning of the list and all odd numbers to the end.
# given = [1, 2, 3, 4, 5, 6]
# evens = [x for x in given if x%2==0]
# odds = [x for x in given if x%2!=0]
# even_odd = evens + odds
# print(even_odd)
#---------------------------------------------------------------------------------------------------
# Given a list and an integer k, rotate the list to the left by k positions. For example,
# if k=2, the first two elements move to the end of the list.
# nums = [1, 2, 3, 4, 5]
# k = 2
# for _ in range(k):
#     # Remove the first element
#     first_element = nums.pop(0)
#     # Move it to the end
#     nums.append(first_element)
#
# print("Rotated List:", nums)

#---------------------------------------------------------------------------------------------------
# Write a program to display the Fibonacci sequence up to 10 terms. The sequence starts with 0 and 1, and each
# subsequent number is the sum of the two preceding ones.
# Given Input: n_terms = 10
# Expected Output: 0 1 1 2 3 5 8 13 21 34

# First two terms
# num1, num2 = 0, 1
#
# print("Fibonacci sequence:")
# for _ in range(10):
#     print(num1, end="  ")
#     # Calculate next term
#     res = num1 + num2
#     # Update values for next iteration
#     num1 = num2
#     num2 = res


#---------------------------------------------------------------------------------------------------
# Write a program to check if a number is a “Perfect Number.” A perfect number is a positive integer that is equal to
# the sum of its proper divisors (excluding the number itself). For example, 6 is perfect because 1 + 2 + 3 = 6.

# def is_perfect_num(n):
#     divisors = []
#     for i in range(1, n):
#         if n % i == 0:
#             divisors.append(i)
#     print(f'{n} is perfect number: {True if sum(divisors) == n else False}')
# is_perfect_num(28)

#---------------------------------------------------------------------------------------------------
# Write a program to display all prime numbers within a range (e.g., 25 to 50). A prime number is a natural number
# greater than 1 that is not a product of two smaller natural numbers.
# start = 25
# end = 50
#
# for num in range(start, end+1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)

#---------------------------------------------------------------------------------------------------
# Write a program to calculate the sum of the series 2 + 22 + 222 + 2222 + …. up to N terms. For example,
# if n=5, the series is 2 + 22 + 222 + 2222 + 22222.
number_of_terms = 5
num = 2
result = 0
# expected out put = 24690
for i in range(1, number_of_terms+1):
    strnum = int(str(num) * i)
    print(strnum)
    result += strnum

print(result)

#---------------------------------------------------------------------------------------------------
# Given a nested list (a list containing other lists), write a program to “flatten” it into a single
# list containing all the individual elements.
# nested_list = [[10, 20], [30, 40], [50, 60]]
# flattened_list = [x for y in nested_list for x in y]
# print(flattened_list)
#---------------------------------------------------------------------------------------------------
# Given a 2D list (matrix), find the row and column index of a target value.
# matrix = [[10, 20], [30, 40], [50, 60]]
# target = 40
# expected result: Target 30 found at Row: 1, Column: 0
# for i, row in enumerate(matrix):
#     for j, col in enumerate(row):
#         if col == target:
#             print(f'Target {target} found at row {i} and col {j}')

#---------------------------------------------------------------------------------------------------