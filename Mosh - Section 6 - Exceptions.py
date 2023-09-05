"""This is section 6 of Mosh's course."""

from traitlets import This


numbers = [1, 2]
print(numbers[3])

# Above is an instance of thrown exception


# %%

# How can we handle exceptions?


try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError as something:
    print("Please enter a valid age.")
    print(something)
else:
    print("I don't know when this is printed.")


# %%

# Handling different exceptions

try:
    age = int(input("Enter your age: "))
    x_factor = 10 / age
    print(age)

except (ValueError, ZeroDivisionError) as something:
    print("Please enter a valid age.")
    print(something)

else:
    print("This is printed at the end when no exception is thrown.")

# %%

# Code Cleanup

try:
    file = open("Mosh - Section 6 - Exceptions.py", mode="r")
    age = int(input("Enter your age: "))
    x_factor = 10 / age
    print(age)

except (ValueError, ZeroDivisionError) as something:
    print("Please enter a valid age.")
    print(something)

else:
    print("This is printed at the end when no exception is thrown.")

finally:
    file.close()
    print("This message will be printed regardless of the input.")

# %%


try:
    with open("Mosh - Section 6 - Exceptions.py") as file1, open(
        "Mosh - Section 5 - Data Structures.py"
    ) as file2:
        print("Both files are opened.")

    age = int(input("Enter your age: "))
    x_factor = 10 / age
    print(age)

except (ValueError, ZeroDivisionError) as something:
    print("Please enter a valid age.")
    print(something)

else:
    print("This is printed at the end when no exception is thrown.")

finally:
    file.close()
    print("This message will be printed regardless of the input.")


# %%

# Raising Exceptions


def calculate_x_factor(age):
    """This function calculates the x factor."""
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return age / 10


try:
    calculate_x_factor(0)
except ValueError as this_error:
    print(this_error)


# %%

# Cost of raising exceptions

from timeit import timeit


CODE1 = """
def calculate_x_factor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return age / 10


try:
    calculate_x_factor(0)
except ValueError as this_error:
    print(this_error)
"""

CODE2 = """
def calculate_x_factor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return age / 10


try:
    calculate_x_factor(0)
except ValueError as this_error:
    pass
"""

CODE3 = """
def calculate_x_factor(age):
    if age <= 0:
        return None
    return age / 10

x_factor = calculate_x_factor(0)
if x_factor == None:
    pass
"""

print("It takes:", timeit(CODE1, number=1000))
print("It takes:", timeit(CODE2, number=1000))
print("It takes:", timeit(CODE3, number=1000))


# %%
