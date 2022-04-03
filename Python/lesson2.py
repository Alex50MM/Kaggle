'''
https://www.kaggle.com/code/colinmorris/functions-and-getting-help
'''

# Getting help
# 1
help(round)

# 2
help(round(-2.01))


# 3
help(print)

# 4
def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

# 5
print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)
# Python allosw trailing comas in argument lists. How nice is that?

# 6
help(least_difference)

# 7
def least_difference(a, b, c):
    ''' Return the smallest difference between any two numbers
    among a, b and c.

    >>> least_difference(1, 5, -5)
    4
    '''
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

# 8
help(least_difference)

# 9
def least_difference(a, b, c):
    ''' Return the smallest difference between any two Numbers
    among a, b and c.
    '''
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    min(diff1, diff2, diff3)

print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)

# 10
mystery = print()
print(mystery)

# 11
print(1, 2, 3, sep= ' < ')

# 12
print(1, 2, 3)

# 13
def greet(who= 'Colin'):
    print('Hello', who)

greet()
greet(who= 'Kaggle')
# (In this case, we don't need to specify the name of the argument, becauseit's unambiguos.)
greet('world')

# 14
def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    ''' Call fn on arg '''
    return fn(arg)

def squared_call(fn, arg):
    ''' Call fn on the result of calling fn on arg '''
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep= '\n', # '\n' is the new line character - it starts a new line
)

# 15
def mod_5(x):
    ''' Return the reminder of x after dividing by 5 '''
    return x % 5

print(
    'Which number is biggest? ',
    max(100, 51, 14),
    'Which number is the biggest modulo 5? ',
    max(100, 51, 14, key= mod_5),
    sep= '\n',
)
