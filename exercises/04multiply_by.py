# Write a function called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.
#
# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a function,
# need a return statement, need a for loop to iterate over the array.
#
# Example function call:
#
# multiply_by([1, 2, 3], 5)
#
# > [5, 10, 15]

def multiply_by(list,multiplier):
    new_list = [number * multiplier for number in list]
    print(new_list) 

#  OR CAN SOLVE WITH

def multiply_by_v2(list,multiplier):
    new_list = []
    for number in list:
        new_list.append(number * multiplier)
    print(new_list)

multiply_by([1, 2, 3], 5)
print('-' * 20)
multiply_by_v2([1, 2, 3], 5)