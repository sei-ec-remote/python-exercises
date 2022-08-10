# Write a function called `p_times` that takes a `statement` and
# a `num` as inputs, and outputs the `statement` some `num` of times
# to the console.
#
# Example function call:
#
# p_times('Hello there', 1)
#
# > Hello there
#
# p_times('Hello there', 3)
#
# > Hello there
# > Hello there
# > Hello there

def p_times(phrase, number):
    print(f'{phrase}\n' * number)

p_times('Hello there', 1)
p_times('Hello there', 3)