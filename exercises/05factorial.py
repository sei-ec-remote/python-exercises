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
def factorial(n):
    factorial_list = []
    result = 1
    for i in range(1, n+1):
        factorial_list.append(i)
    for number in factorial_list:
        result = number * result
        # don't need to return it - it does so already
        # print(result) 
    # print(factorial_list)
    print(result)

factorial(5)