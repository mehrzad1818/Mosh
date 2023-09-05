"""Python is the best."""


letters = ["a", "b", "c"]
matrix = [[0, 1]]
zeros = [0] * 5
combined = zeros + letters
print(combined)
numbers = list(range(21))
chars = list("Hello World")
print(len(chars))

# %%
# Part 2 - Accessing Items
letters = list("abcd")
# alphabet = set(list("thequickbrownfoxjumpsoverthelazydog"))
# print(len(alphabet))
letters[3] = "D"
print(letters)

print(letters[0:3:2])
print(letters[0::2])
print(letters[-1::-1])


new_numbers = list(range(21))

print(new_numbers[::2])
print(new_numbers[::-2])
print(new_numbers[::-1])
print(new_numbers[::1])

# %%
numbers = list(range(21))
first, second, third = numbers


first, second, *this = numbers


# What just happened above is just like what we did in multiply function:


def multiply(*numbers):
    """It multiplies."""
    total = 1
    for number in numbers:
        total *= number
    return total


print(
    multiply(
        5195154245245245245294851,
        418452424524245424125846,
        464642424524524552452542454,
        536344524524592452424524524563,
        23342422245245452523452345,
        234525424529542452453452345,
        232445254245524524524546,
        6452544522542542542452547,
        42452542452445245245524525,
        45645694524529252242542542465,
        7897842452452452425673423,
        2344524524525425245439992,
    )
)

print(first)
print(second)
print(this)

# The code above is the same as the code below.

first = numbers[0]
second = numbers[1]
third = numbers[2]


# %%
# Here we learn more new things about lists:


letters = ["a", "b", "c", "d", "e", 23, 46, True]

for index, letter in enumerate(letters):
    print(f"{index} {letter} {type(letter)}")

# %%

# append method is used to add items to the end of a list


letters = ["a", "b", "c"]

# Add

letters.append("d")
letters.insert(0, "-")


# Remove
letters.pop(0)
letters.remove("b")
del letters[0:3]
letters.clear()
print(letters)


# %%
# Finding items:


letters = ["a", "b", "c"]
print(letters.count("d"))
print(letters.index("a"))
if "h" in letters:
    print(letters.index("h"))

# %%
# Sorting Lists


numbers = [23, 56, 1, 34, 87, 234]
# numbers.sort(reverse=True)
print(sorted(numbers, reverse=True))
print((numbers))


# the difference between sort method and sorted function is that
# the latter returns a new list with sorted items.

# How can we sort tuples???

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 23),
]


def sort_item(item):
    """Makes items a list"""
    return item[1]


items.sort(key=sort_item)
print(items)


# There's a more efficient way for the above code.
# %%


# Lambda function
# lambda arguments : expression


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 23),
]


items.sort(key=lambda item: item[1])
print(items)

# %%

# Mapping function (lambda)
# lambda arguments : expression

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 23),
]


prices = []
for item in items:
    prices.append(item[1])

print(prices)

# This is one basic way of mapping data into a new data type.

# Below is the more advanced format:

prices = list(map(lambda item: item[1], items))
print(prices)

# %%
# Filter function
# lambda arguments : expression

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 23),
]


overpriced = list(filter(lambda james: james[1] >= 10, items))
print(overpriced)

# %%


# List Comprehension
# [Expression for something in somethings]

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 23),
]


prices = list(map(lambda item: item[1], items))
print(prices)
prices = [item[1] for item in items]
print(prices)


overpriced = list(filter(lambda james: james[1] >= 10, items))
print(overpriced)

overpriced = [item[1] >= 10 for item in items]
print(overpriced)

overpriced = [item for item in items if item[1] >= 10]
print(overpriced)

# %%

# Zip Function

list1 = [1, 2, 3, 4, 5, 6]
list2 = [10, 20, 30, 40, 50, 60]


print(list(zip("abcdef", list1, list2)))

# %%

# Stack (Stack of items, LIFO)

# LIFO -> Last in - First out


browsing_session = []

browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

print(browsing_session)

last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])

if not browsing_session:
    print("disable")

# %%

# Queue

# FIFO -> First in First out

# from module import class

from collections import deque

queue = deque([])

queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")

# %%

# Tuples
# A read only list (Can't be modified)

point = (1, 2)
three_points = (1, 2) + (3, 5)

print(point)
print(three_points)
print(three_points[1:2])

w, x, y, z = three_points
print(y)
print(w)

if 10 in point:
    print("exists")
# %%

# Swapping Variables


x = 10
y = 11

print(x, y)


z = x
x = y
y = z

print(x, y)


x, y = y, x

print(x, y)


# %%


# Arrays
from array import array


numbers = array("i", [1, 2, 3, 4, 5, 6])
print(numbers[0])

print(numbers)

# %%

# Sets


numebrs = [1, 3, 4, 5, 2, 1, 2, 4, 5, 7, 7]
first = set(numbers)
print("first:", first)

second = {1, 4}
second.add(56)
second.remove(1)
print("second:", second)


uni = first | second
print("unison:", uni)

intersect = first & second
print("intersection:", intersect)

print("only in first:", first - second)
print("only in second:", second - first)
print("unique items in each set:", first ^ second)


# %%

# Dictionary


point = {"x": 1, "y": 2}

point = dict(w=34, x=12, y=61, z=1)
print(point)


point["x"] = 10
point["z"] = 20

if "a" in point:
    print(point["a"])

print(point.get("a", 0))
del point["x"]

print(point)


for key in point:
    print(key, point[key])

for key, value in point.items():
    print(key, value)


# %%


# Dictionary Comprehension

# inefficient way
values = []
for x in range(5):
    values.append(x * 2)
print(values)

# more efficient way
list_values = [x * 2 for x in range(5)]
print(list_values)


# This can be used for sets and dictionaries, too.

dict_values = {x: x**2 for x in range(101)}
print(dict_values)


set_values = (x**2 for x in range(101))
print(set_values)
# %%

# Generator Expressions

from sys import getsizeof

list_values = [x * 2 for x in range(5000)]
print(list_values)
print(getsizeof(list_values))

set_values = (x**2 for x in range(5000))
print(set_values)
print(getsizeof(set_values))

# %%


# Unpacking Operator

# By just adding an asterisk before the argument,
# we can print single items individually

numbers = [1, 2, 3]
print(numbers, sep="23", end="43")
print(*numbers)
print(numbers)
print(*numbers)
print(1, 2, 3)


values = list(range(5))
print(*values)

values = [*range(5)]
print(values)

values = [range(5)]
print(values)

values = [*range(5), *"Hello World"]
print(values)

# We can use one asterisk to unpack lists,
# We can use two asterisks to unpack dictionaries,

# %%


# QUIZ TIME
from pprint import pprint

sentence = "this might be the last time I'm going to play with myself."

counter = {}

for letter in sentence:
    if letter in counter:
        counter[letter] += 1

    else:
        counter[letter] = 1

char_freq_sorted = sorted(counter.items(), key=lambda kv: kv[1], reverse=True)

print(char_freq_sorted[1])

# %%
