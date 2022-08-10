# Write a function to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1

def factorial(num):
    for i in range(1,num):
        num = num * i
    return print(num)

# Example function call
#
factorial(5)
#
# > 120
#
factorial(12)
