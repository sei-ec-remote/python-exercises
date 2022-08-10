# Write a function called `letter_count` to count the letter
# occurrence in a string. Use a dictionary.

def letter_count(string):
    dd = {}
    for letter in string:
        if dd.get(letter):
            dd[letter]= dd[letter] + 1
        else: dd[letter] = 1
    print(dd)
        

# You can iterate over a string one letter at a time using
# a for loop.
#
# for letter in "alpha":
#   print(letter)
#
# Create a dictionary with `dd = {}`. Assign values with `dd["foo"] = 1`.
# Check to see if a dictionary has a key using the `in` operator.
#
#
# Careful. Python requires that you insert a key into a dictionary
# before you try to modify it's value. If you try to access a dictionary
# at a key that hasn't been added you'll get an error and the program will
# crash. Remember to use an if statement to see if a key is "in" a dictionary
# before you try to read it!
#
# d2 = {}
# d2["foo"]
# > KeyError: 'foo'
#
# Example function call:
#
letter_count('banana')
letter_count('what is up')
letter_count("what's up")
#
# > {'a': 3, 'b': 1, 'n': 2}
