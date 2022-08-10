# Write a function called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.
#
# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a function,
# need a return statement, need a for loop to iterate over the array.

def multiply_by(list, number):
    edited_list = [this_num * number for this_num in list]
    return print(edited_list)


# Example function call:
#
multiply_by([1, 2, 3], 5)
#
# > [5, 10, 15]

multiply_by([3, 6, 9], 5)