# Write a function to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example function call
#
# factorial(5)
#
# > 120
#
def factorial(num):
    product = 1
    for i in range(1, num+1):
        product *= i
    print(product)

factorial(5)

# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return (num) * factorial(num - 1)

# print(factorial(5))