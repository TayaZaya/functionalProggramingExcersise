from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def item_capitalize(item):
    return item.upper()


print(list(map(item_capitalize, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
my_numbers.sort()
print(list(zip(my_strings, my_numbers)))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def overthithty(item):
    return item > 50


print(list(filter(overthithty, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
from functools import reduce


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, (my_numbers + scores)))

# 5 lambda function-print all odd numbers in my_numbers
print(list(filter(lambda item: item % 2 != 0, my_numbers)))

from functools import reduce

print(reduce(lambda acc, item: acc + item, my_numbers))

# 6 return a list that squares my_list2
my_list2 = [5, 4, 3]

print(list(map(lambda item: item * item, my_list2)))

# 7 list sorting of a list of tuples by the second index

a = [(0,2), (4,3), (9,9), (10,-1)]

a.sort(key=lambda x: x[1])
print(a)

# list comprehensions-- making a list out of a given string+
# capitalizing the whole string:
my_pets = [char for char in 'dobbie'.upper()]
print(my_pets)

# dictionary comprehensions
# 1 making a dict with the numbers in the list as the keys
# and the numbers * 2 as the values

my_dict = {num: num * 2 for num in [1,2,3]}
print(my_dict)

# exercise - comprehensions:

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates =list(set([item for item in some_list if some_list.count(item) >1]))

print(duplicates)
#or:

duplicates = [item for item in some_list if some_list.count(item) >1]
duplicates2 = list(set(duplicates))

print(duplicates2)


