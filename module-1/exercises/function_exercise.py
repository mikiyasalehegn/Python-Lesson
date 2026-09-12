# Create a function show_employee() that accepts an employee’s name and salary. If the salary is not provided in the
# function call, the function should automatically assign a default value of 9000.
# def show_employee(name, salary=9000):
#     print(f'Name: {name}, Salary: {salary}')
#
# show_employee(name='Mike', salary=10000)
# show_employee(name='Abel')

# -------------------------------------------------------------------------------------------------------------------
# Create an outer function that accepts two parameters, a and b. Inside, create an inner function that calculates
# the addition of a and b. The outer function should then add 5 to that sum and return the final result.

# def outer(a,b):
#     def inner():
#         return a+b
#     final_result = inner() + 5
#     return final_result
#
# print(outer(10,5))

# -------------------------------------------------------------------------------------------------------------------
#  Write a recursive function addition() that calculates the sum of numbers from 0 to 10. A recursive function is a
#  function that calls itself to solve smaller instances of the same problem.
# def addition(num):
#     if num == 0:
#         return 0
#     return num + addition(num - 1)
#
# print(addition(10))
# -------------------------------------------------------------------------------------------------------------------
# Assign a different name to the function display_student(name, age) and call it using the new name. For example,
# assign it to a variable called show_student.
# def student_info(name, age):
#     return f'Student name: {name} age: {age}'

# student_show = student_info('John', 25)
# print(student_show)

# -------------------------------------------------------------------------------------------------------------------
# def find_max(nums):
#     max_num = 0
#     for item in nums:
#         if item > max_num:
#             max_num = item
#     return max_num
#
# print(find_max([4, 6, 8, 24, 12, 2]))

# -------------------------------------------------------------------------------------------------------------------
# Define a function describe_pet(animal_type, pet_name) that prints a description of a pet. Call this function twice:
# once using positional arguments and once using keyword arguments.
# def describe_pet(animal_type, pet_name):
#     print(f'Ihave a {animal_type}\nMy {animal_type}\'s name is {pet_name}')
#
# describe_pet('Dog', 'Jack')
# describe_pet(animal_type='Hamster', pet_name='Tommy')
# -------------------------------------------------------------------------------------------------------------------
# Create a function print_info(**kwargs) that accepts an arbitrary number of keyword arguments and prints the key-value pairs.
# def print_info(**kwargs):
#     for key, val in kwargs.items():
#         print(f'{key}: {val}')

# def print_info(name, age, city):
#     print(f'{name} is {age} years old and lives in {city}.')
# info = {'name':'Mike', 'age':29, 'city':'Rishon Letsyon'}
# print_info(**info)
# -------------------------------------------------------------------------------------------------------------------
# Write a recursive function to calculate the factorial of a non-negative integer.
# def factorial(n):
#     if n < 0:
#         raise ValueError('Factorial doesn\'t support negative number')
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
#
# try:
#     print(factorial(-1))
# except ValueError as e:
#     print(e)
#
# print('done!')
# -------------------------------------------------------------------------------------------------------------------
# Use the lambda keyword to create a small, anonymous function that takes one number and returns its square.
# square = lambda x: x ** 2
# print(square(5))

# -------------------------------------------------------------------------------------------------------------------
# Use the filter() function combined with a lambda to extract all even numbers from the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = list(filter(lambda x : x % 2 == 0, num_lst))
# print(evens)
# -------------------------------------------------------------------------------------------------------------------
# Use the map() function and a lambda to double every element in the list [1, 2, 3, 4, 5].
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# double_nums = list(map(lambda x : x * 2, num_list))
# print(double_nums)

# -------------------------------------------------------------------------------------------------------------------
# You have a list of tuples representing students and their grades: [("Alice", 88), ("Bob", 75), ("Charlie", 92)].
# Use the sorted() function and a lambda to sort this list based on the grades (the second element) in ascending order.
grades = [("Alice", 88), ("Bob", 75), ("Charlie", 92)]
# grades.sort(key=lambda grade: grade[1])
# print(grades)

# sorted_drages = sorted(grades, key=lambda grade: grade[1], reverse=False)
# print(sorted_drages)

# -------------------------------------------------------------------------------------------------------------------
# Write a function apply_operation(func, x, y) that takes another function (func) and two numbers (x, y) as arguments.
# It should return the result of calling func(x, y). Show how this works by passing in different operations like
# addition and multiplication.
# def apply_operation(func, a , b):
#     return func(a, b)
#
# add = lambda a, b: f'Addition result: {a + b}'
# mult = lambda a, b: f'Multiplication result: {a * b}'
# add_result = apply_operation(add, a=4, b=5)
# print(add_result)
# mult_result = apply_operation(mult, a=4, b=5)
# print(mult_result)
# -------------------------------------------------------------------------------------------------------------------
# Write a lambda that takes a single integer and returns the string "even" if the number is divisible by 2, or "odd"
# otherwise. Assign it to a variable named parity and test it on several values.
# even_odd = lambda x: 'Even' if x % 2 ==0 else 'Odd'
# print(even_odd(10))
# -------------------------------------------------------------------------------------------------------------------
# Store four lambda functions in a dictionary under the keys "add", "sub", "mul", and "div". Each lambda should
# take two numbers and perform the corresponding arithmetic operation. Use the dictionary to build a simple calculator
# that looks up the operation by key and applies it to two operands.

# ops = {
#     'add': lambda a, b : a + b,
#     'subtract': lambda a, b: a - b,
#     'multiply': lambda a, b: a * b,
#     'divide': lambda a, b: a / b
# }
#
# val1,val2 = 5, 4
# for name, func in ops.items():
#     print(f'{name}: {func(val1, val2)}')

# -------------------------------------------------------------------------------------------------------------------
# Given a list of employee dictionaries, each with a "name" and a "salary" key, sort the list by salary in descending order.
# Where two employees share the same salary, sort those entries by name in ascending alphabetical order.
# Use a single lambda as the key argument

# employees = [{"name": "Alice", "salary": 70000}, {"name": "Bob", "salary": 90000}, {"name": "Charlie", "salary": 70000},
#              {"name": "Diana", "salary": 90000}]
# ordered = sorted(employees, key=lambda e: (-e['salary'], e['name'] ))
# print(ordered)

# -------------------------------------------------------------------------------------------------------------------
# Write a general multiply(x, n) function that returns x * n. Use functools.partial() to create two specialised functions from it: double(x),
# which always multiplies by 2, and triple(x), which always multiplies by 3. Call both with several values.
# from functools import partial
#
# def multiplier(x, n):
#     return x * n
#
# num = 5
# double = partial(multiplier, 2)
# print(double(num))
# triple = partial(multiplier, 3)
# print(triple(num))

# -------------------------------------------------------------------------------------------------------------------
# Write a compose(f, g) utility function that returns a new function equivalent to applying g first and then f to the
# result — that is, compose(f, g)(x) should equal f(g(x)). Test it by composing a lambda that doubles a number with
# a lambda that adds 3.
# def compose(f, g):
#     return lambda x: f(g(x))
#
# double = lambda x: x * 2
# add_3 = lambda x: x + 3
#
# double_after_add = compose(double, add_3)
# print(double_after_add(5))
# -------------------------------------------------------------------------------------------------------------------
# Given a list of lists, use functools.reduce() with a lambda to flatten it into a single list. Do not use any f
# or loops, list comprehensions, or itertools.
# from functools import reduce
# nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
#
# flat_list = list(reduce(lambda x, y: x + y, nested))
# print(flat_list)

import time
from functools import lru_cache
# fibonacci_cached = {}
# def fib(n):
#     if n in fibonacci_cached:
#         return fibonacci_cached[n]
#     if n <= 1:
#         return n
#     fibonacci_cached[n] = fib(n-1) + fib(n-2)
#     return fib(n - 1) + fib(n - 2)
#
# for num in range(1, 101):
#     print(f'{num}: {fib(num)}')

# Cached result
# @lru_cache(maxsize=200)
# def cached_fib(n):
#     if n < 0:
#         raise ValueError('n must be positive integer!')
#     if type(n) != int:
#         raise TypeError('n must be a positive integer!')
#     if n <= 1:
#         return n
#     return cached_fib(n-1) + cached_fib(n-2)
#
#
# # non cached result
# def uncached_fib(n):
#     if n < 0:
#         raise ValueError('n must be positive integer!')
#     if type(n) != int:
#         raise TypeError('n must be a positive integer!')
#     if n <= 1:
#         return n
#     return uncached_fib(n-1) + uncached_fib(n-2)
#
# # cached
# cached_start = time.perf_counter()
# cached_fib = cached_fib(35)
# cached_fib_len = time.perf_counter() - cached_start
#
# # uncached
# uncached_start = time.perf_counter()
# uncached_fib = uncached_fib(35)
# uncached_fib_len = time.perf_counter() - uncached_start
#
# print(f'cached:{cached_fib}, cached_fib_len: {cached_fib_len:.6f}')
# print(f'uncached_fib: {uncached_fib}, uncached_fib_len: {uncached_fib_len:.6f}')
# *******************************************************************************************************************
# You are climbing a staircase with n steps. You are given an array cost where cost[i] represents the price of step i.
# Once paid, you can take 1 or 2 steps. You can start at index 0 or index 1.
# Write a function min_cost_climbing_stairs(cost) that returns the minimum total cost to reach the top
# (past the end of the array).Example 1: cost = [10, 15, 20]  Output: 15 (Pay 15 at index 1 right arrow
# step 2 steps to the top)Example 2: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1] : 6
# from functools import lru_cache
#
# cost_step = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
#
# @lru_cache(maxsize=None)
# def min_cost_climbing_stairs(cost):
#     for index, cost in enumerate(cost_step):
#         total_price = min_cost_climbing_stairs(cost)
# *******************************************************************************************************************
# You are climbing a staircase with n steps. You are given an array cost where cost[i] represents the price of step i.
# Once paid, you can take 1 or 2 steps. You can start at index 0 or index 1.
# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# def min_cost_climbing_stairs(costs: list)-> int:
#     def cost_steps(index):
#         if index >= len(costs):
#             return 0
#         min_cost_one_step = cost_steps(index)
#         min_cost_two_steps = cost_steps(index + 1)

from functools import lru_cache

# memo={}
# def min_cost_climbing_stairs(cost: list[int]) -> int:
    # @lru_cache(maxsize=None)
    # def min_cost_from(index: int) -> int:
        # Base Case: Reached or passed the top of the stairs
        # if index >= len(cost):
        #     return 0

        # Choice: Pay current step cost, then pick the cheaper path (1 step or 2 steps)
        # take_one_step = min_cost_from(index + 1)
        # take_two_steps = min_cost_from(index + 2)
        # result = cost[index] + min(take_one_step, take_two_steps)
        # memo[index] = result
        # return result

    # You can start at index 0 OR index 1
    # total_cost = min(min_cost_from(0), min_cost_from(1))

    # Print cache statistics to inspect performance
    # print(memo)

    # return total_cost

# print("Test 1 Result:", min_cost_climbing_stairs([10, 15, 20]))
# print("\nTest 2 Result:", min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))


# *******************************************************************************************************************
# Given a list of (name, age) tuples, sort them in ascending order by age using sorted() with a lambda as the key
# argument. Then sort the same list in descending order by age.

# people = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("Diana", 28)]
# order_by_age = sorted(people, key=lambda person: person[1], reverse=True)
# print(order_by_age)

# *******************************************************************************************************************
# Use map() with a lambda to convert a list of temperatures from Celsius to Fahrenheit. The conversion formula is
# F = (C × 9/5) + 32. Collect the results into a new list and print it.

# celsius = [0, 20, 37, 100]
# fahrenheit = list(map(lambda temp: (temp * 9/5) + 32, celsius))
# print(fahrenheit)

# *******************************************************************************************************************
# Use functools.reduce() with a lambda to find the product of all numbers in a list. The function should multiply each
# element cumulatively from left to right until a single value remains.
# from functools import reduce
#
# numbers = [1, 2, 3, 4, 5]
# products = reduce(lambda a, b: a*b, numbers)
# print(products)
# *******************************************************************************************************************
#  Write a lambda that takes a single integer and returns the string "even" if the number is divisible by 2, or "odd"
#  otherwise. Assign it to a variable named parity and test it on several values.
# even_or_odd = lambda num: "even" if num % 2 == 0 else "odd"
# print(even_or_odd(50))
# *******************************************************************************************************************
# operators = {
#     "add": lambda a, b : a+b,
#     "sub": lambda a, b : a-b,
#     "mul": lambda a, b : a*b,
#     "div": lambda a, b : round(a/b, 2),
# }
#
# x,y = 5,6

# for operation, func in operators.items():
#     print(f'{operation} {x} and {y} = {func(x,y)}')

# addition = operators["add"](2,4)
# print(addition)

# *******************************************************************************************************************
# Given a list of employee dictionaries, each with a "name" and a "salary" key, sort the list by salary in descending order.
# Where two employees share the same salary, sort those entries by name in ascending alphabetical order.
# Use a single lambda as the key argument.

# employees = [
#     {"name": "Alice", "salary": 70000},
#     {"name": "Bob", "salary": 90000},
#     {"name": "Charlie", "salary": 70000},
#     {"name": "Diana", "salary": 90000}
# ]
#
# sorted_employees = sorted(employees, key=lambda employee: (-employee['salary'], employee['name']))
# print(sorted_employees)

# *******************************************************************************************************************
# Write a general multiply(x, n) function that returns x * n. Use functools.partial() to create two specialised
# functions from it: double(x), which always multiplies by 2, and triple(x), which always multiplies by 3.
# Call both with several values.
# from functools import partial
#
# def multiply(x, n):
#     return x*n
#
# double = partial(multiply, 2)
# print(double(2))
# triple = partial(multiply, 3)
# print(triple(4))

# *******************************************************************************************************************
# Write a compose(f, g) utility function that returns a new function equivalent to applying g first and then f to the
# result — that is, compose(f, g)(x) should equal f(g(x)). Test it by composing a lambda that doubles a number
# with a lambda that adds 3.

# def compose(f, g):
#     return lambda x: f(g(x))
#
# add_two_first = lambda x: x + 2
# double_next = lambda x: 2*x
#
# result = compose(g=add_two_first, f=double_next)
# print(result(3))

# *******************************************************************************************************************
# Given a list of lists, use functools.reduce() with a lambda to flatten it into a single list.
# Do not use any for loops, list comprehensions, or itertools.
# from functools import reduce
#
# nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
#
# flatten_list = list(reduce(lambda x, y: x+y , nested))
# print(flatten_list)

# *******************************************************************************************************************
# Given a list of strings, sort them alphabetically by their last character using a lambda as the key argument to
# sorted(). Where two strings end with the same character, preserve their original relative order.
# words = ["banana", "apple", "cherry", "date", "fig", "kiwi"]
# ordered_words = sorted(words, key=lambda word: (word[-1], word[0]))
# print(ordered_words)

# *******************************************************************************************************************
# Implement your own versions of my_map(func, lst), my_filter(pred, lst), and my_reduce(func, lst, initial) from scratch
# using only recursion and lambdas. No loops, no built-in map/filter/reduce, and no list comprehensions.
# Verify each against a known input.
# numbers = [1, 2, 3, 4, 5]

# def my_map(func, iterable):
#     lst = []
#     if iterable:
#         for item in iterable:
#             lst.append(func(item))
#     return lst
#
# double_items = my_map(lambda a: a*2, numbers)
# print(double_items)

# *******************************************************************************************************************
# *******************************************************************************************************************
# *******************************************************************************************************************
# *******************************************************************************************************************