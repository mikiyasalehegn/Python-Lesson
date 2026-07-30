### 1/ Write a program to create a new string made of an input string’s first, middle, and last characters.
# Example:
# given string ==> 'James'
# The output = 'Jms'

# def first_middle_last():
# given_str = str(input('Enter any string: '))
#     if len(given_str) == 0:
#         print( 'You entered an empty string')
#     else:
#         print( given_str if len(given_str) in [1,2] else f'{given_str[0]}{given_str[len(given_str)//2]}{given_str[len(given_str)-1]}')
# first_middle_last()

#---------------------------------------------------------------------------------------------------------------------

### 2/ This builds on indexing by introducing String Slicing. Slicing is a powerful Python feature that lets you extract entire “chunks” of data efficiently.
# Example:
# Given str => JhonDipPeta
# output => Dip

# def middle_3():
#     given_str = str(input('Enter any string: '))
#     if len(given_str) < 3:
#         print('String must be at least 3 characters.')
#     midpoint = len(given_str) // 2
#     print(f'The middle are {given_str[midpoint-1:midpoint+2]}')
# middle_3()

# --------------------------------------------------------------------------------------------------------------------

### 3/ Given two strings, s1 and s2, create a new string from the first, middle, and last characters of each input string.
# Given Input: s1 = "America" s2 = "Japan"
# Expected Output: AJrpan

# def combine_2_strs():
#     str1 = str(input("Enter first string: "))
#     str2 = str(input("Enter second string: "))
#
#     if len(str1) < 3 or len(str2) < 3:
#         return "String must be at least 3 characters."
#     middle_point1 = len(str1) // 2
#     middle_point2 = len(str2) // 2
#     return  f'new string: {str1[0]}{str2[0]}{str1[middle_point1]}{str2[middle_point2]}{str1[-1]}{str2[-1]}'
#
# new_str = combine_2_strs()
# print(new_str)

#--------------------------------------------------------------------------------------------------------------------

# Write a program to find the last index of the substring “Emma” in a given string.
# Given Input: str1 = "Emma is a data scientist who knows Python. Emma works at google."
# Expected Output: Last occurrence of Emma starts at index 43
# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# to_find = 'Emma'
# index_of_emma = str1.rfind(to_find) #*** rfind() does the reverse find and return the first index
# print(f'The last occurrence of `Emma` starts at index {index_of_emma}')

#--------------------------------------------------------------------------------------------------------------------
# Write a program to find the total count of the substring “USA” in a given string,
# ignoring the case (i.e., both “usa” and “USA” should be counted).
# Given Input: str1 = "Welcome to USA. usa awesome, isn't it?"
# Expected Output: The USA count is: 2
# str1 = "Welcome to USA. usa awesome, isn't it?".lower()
# to_count = 'usa'
# print(f'The USA count is:{str1.count(to_count)}')

#--------------------------------------------------------------------------------------------------------------------
# Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced
# if all the characters in s1 are present in s2. The character’s position doesn’t matter.
# Given Input:
# Case 1: s1 = "yn", s2 = "PyNative"      ## True
# Case 2: s1 = "ynf", s2 = "PyNative"     ## False

# def string_balance_check(s1, s2):
#     is_balanced = True
#     for char in s1:
#         if char not in s2:
#             is_balanced = False
#             break
#
#     return f' Are {s1} and {s2}? {is_balanced}'
#
# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
# print(string_balance_check(str1, str2))

#--------------------------------------------------------------------------------------------------------------------
# Write a program to count the total number of vowels (a, e, i, o, u) in a given string.
# Given Input: str1 = "Hello World"
# Expected Output: Vowel Count: 3

# def vowl_counter(string):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     vowel_count=0
#     for char in vowels:
#         if char in string:
#             amount = string.count(char)
#             vowel_count += amount
#     print(f'{vowel_count} vowels were found')
#
# vowl_counter('Hello World')

#--------------------------------------------------------------------------------------------------------------------
# Remove every single space from a given string, including spaces between words.
# Given Input: str1 = " P y t h o n "
# Expected Output: Python

# s1 = ' P y t h o n'
# new_string = s1.replace(' ', "")
# print(new_string)
#--------------------------------------------------------------------------------------------------------------------
# Write a program to remove the character at index i from a string.
# def char_remover(string, i):
#     chars = list(string)
#     if i <= len(chars):
#         chars.remove(chars[i])
#         print(f'The string with removed character: {"".join(chars)}')
#     else:
#         print('index is out of range')
#
# char_remover('Hello World', 5)
#--------------------------------------------------------------------------------------------------------------------
# Use the .partition() method to split a string into three parts: the part before a separator, the separator itself,
# and the part after it.

# str1 = "username@company.com"   #sep = "@"
# separated = str1.partition("@")
# print(separated)

#--------------------------------------------------------------------------------------------------------------------
# Write a program to arrange string characters such that all lowercase letters come first, followed by all uppercase letters.
# str1 = "PyNaTive"
# strlist = []
# for letter in str1:
#     if letter.islower():
#         strlist.insert(0, letter)
#     else:
#         strlist.append(letter)
#
# lower_first = "".join(strlist)
# print(lower_first)

#--------------------------------------------------------------------------------------------------------------------
# Given a string, run a loop to calculate the sum and average of the digits that appear in the string. Ignore all other characters.
# str1 = "PYnative29@#8496"
# count = 0
# sum_digit = 0
# for char in str1:
#     if char.isdigit():
#         sum_digit += float(char)
#         count += 1
#
# average = sum_digit / count
# print(f'Sum: {sum_digit}, Average: {round(average, 2)}')

#--------------------------------------------------------------------------------------------------------------------
# Count the frequency of every character in a string and store the results in a dictionary.
# str1 = "apple"
#
# char_frequency = {char: str1.count(char) for char in str1}
# print(char_frequency)
#--------------------------------------------------------------------------------------------------------------------
# Write a program to extract only the numeric digits from a mixed string and combine them into a single string.
# str1 = "I am 25 years and 10 months old"
# only_digits = ''
#
# for char in str1:
#     if char.isdigit():
#         only_digits += char
# print(only_digits)


#--------------------------------------------------------------------------------------------------------------------
# Write a program to find and print words from a string that contain both letters and numbers.
# str1 = "Emma25 is Data scientist50 and AI Expert"
# dch = re.findall(r'[A-Z][a-z]+\d+', str1)
# print(f'dch: {dch}')
# strlist = str1.split(" ")
# print(strlist)
# for item in strlist:
#     for char in item:
#         if char.isdigit():
#             print(item)
#             break

#--------------------------------------------------------------------------------------------------------------------
# Write a program to replace every special symbol (punctuation) in a string with a specific character, like #.
# import string
#
#
# str1 = "/*Jon is @developer & musician!!"
# replace_char='#'
# str2 = ''
# for char in str1:
#     if char in string.punctuation:
#         print(char)
#         str1 = str1.replace(char, replace_char)
# print(str1)

# Notice you're using str1 again, not str2.
# So now str2 becomes:
# /#Jon is @developer & musician!!
# The previous replacement (/ → #) is lost.
# This keeps happening until the last special character (!), so the final result is only the last replacement.

#--------------------------------------------------------------------------------------------------------------------
# Write a program to check if a string is a palindrome (reads the same forward and backward).

# def check_palindrome(string):
#     if string == string[::-1]:
#         print(f'IS PALINDROME: True')
#     else:
#         print(f'IS PALINDROME: False')
#
# check_palindrome('radar')
#--------------------------------------------------------------------------------------------------------------------
# Write a program to check if two strings are anagrams (formed by rearranging the letters of another, such as “listen” and “silent”).
# def check_anagrams(s1, s2):
#     return sorted(s1) == sorted(s2)
#
# print(check_anagrams("listen", "silent"))

#--------------------------------------------------------------------------------------------------------------------
# Write a function to determine if a string has all unique characters. Return True if every character appears only once,
# otherwise return False.
# str2 = 'Python'
# unique_chars = True
# for char in str2:
#     if str2.count(char) > 1:
#         unique_chars = False
#
# print(unique_chars)

#--------------------------------------------------------------------------------------------------------------------
# Write a program to remove all duplicate characters from a string while keeping the remaining characters in their original order.
# string1 = 'google translate'
# unique = []
#
# for char in string1:
#     if char not in unique:
#         unique.append(char)
#
# print("".join(unique))
# print(dict.fromkeys(string1))  ## advanced!!

#--------------------------------------------------------------------------------------------------------------------
# Reverse the order of words in a given sentence, but keep the characters within the words in their original order.
# str1 = "Python is fun"
# listed_txt = str1.split(' ')[::-1]
# reversed_text = " ".join(listed_txt)
# print(reversed_text)
#--------------------------------------------------------------------------------------------------------------------
# Given two strings of equal length, merge them by alternating characters.
# Given Input: s1 = "ABC", s2 = "xyz"
# Expected Output: AxByCz
# s1 = "ABC"
# s2 = "xyz"
# combined = ''
# for char1, char2 in zip(s1,s2):
#     combined += char1+char2
# print(combined)

#--------------------------------------------------------------------------------------------------------------------
# Write a program to find the longest word in a given sentence. If there is a tie, return the first one found.
# str1 = "The quick brown fox jumps over the lazy dog"
# str1list = str1.split(" ")
# max_len = max([len(x) for x in str1list])
# longest_words = list(filter(lambda word: len(word) == max_len, str1list))
# print(longest_words[0])
# longest = ''
# for word in str1list:
#     if len(word) > len(longest):
#         longest = word
#
# print(longest)
#--------------------------------------------------------------------------------------------------------------------
# Write a program to generate an acronym from a given phrase (e.g., “Random Access Memory” becomes “RAM”).
# str1 = "Random Access Memory"
# strlist = str1.split(" ")
# acronym = ""
# for char in strlist:
#     acronym += char[0].upper()
# print(acronym)

#--------------------------------------------------------------------------------------------------------------------
# Find the first character in a string that does not repeat anywhere else.
# str1 = "swiss"
# for letter in str1:
#     if str1.count(letter)==1:
#         print(letter)
#         break
#--------------------------------------------------------------------------------------------------------------------
# Write a program to check if one string is a rotation of another (e.g., “waterbottle” is a rotation of “erbottlewat”).
s1 = "waterbottle"
s2 = "erbottlewat"

ordered_s1 = "".join(sorted(s1))
ordered_s2 = "".join(sorted(s2))

if ordered_s1 != ordered_s2:
    print("The strings are not rotated")
else:
    print("The strings are rotated")
    print(ordered_s1)
    print(ordered_s2)


#--------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------