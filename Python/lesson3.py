'''
https://www.kaggle.com/code/colinmorris/booleans-and-conditionals

Para rodar o código no ATOM
usar as teclas CTRL + SHIFT + B
Pode-se rodar somente uma parte do código,
selecionando-o e usando as mesmas teclas de atalho

'''

# Booleans and Conditionals
# 1
x = True
print(x)
print(type(x))


# 2
def can_run_for_president(age):
    """ can someone of the given age run for president in the US"""
    # The US Constitution says you must be at least 35 years old
    return age > 35

print('Can a 19 years old run for president? ', can_run_for_president(19))
print('Can a 45 years old run for president? ', can_run_for_president(45))


# 3
3.0 == 3
print(3.0 == 3)


# 4
'3' == 3
print('3' == 3)


# 5
def is_odd(n):
    return (n % 2) == 1

print('Is 100 odd? ', is_odd(100))
print('Is -1 odd? ', is_odd(-1))


# 6
def can_run_for_president(age, is_natural_born_citizen):
    """ Can someoneof the given age and citizenship status
    run for president is the US """
    # The US Constitution says you must be a
    # natural born citizen "and' at least 35 years old"
    return is_natural_born_citizen and (age >= 35)

print(can_run_for_president(19, True))
print(can_run_for_president(55, False))
print(can_run_for_president(55, True))


# 7
True or True and False
print(True or True and False)


# 8
def inspect(x):
    if x == 0:
        print(x,'is zero.')
    elif x > 0:
        print(x, 'is positive.')
    elif x < 0:
        print(x, 'is negative.')
    else:
        print(x, "is unlike anything i've ever seen...")

inspect(0)
inspect(-15)


# 9
def f(x):
    if x > 0:
        print('Only printed when x is positive; x =', x)
        print('Also only printed when x is positive; x =', x)
    print('Always printed, regardless of x value; x =', x)

f(1)
f(0)


# 10
print(bool(1)) # always numbers are treated as True, except 0
print(bool(0))
print(bool('asf')) # all strings are treated as True, except the empty string ''
''
print(bool('')) # generally empty sequences (strings, lists, and other types
# we've yet to see like list ) and tuples) and 'falsey' and the rest are 'truthy'


# 11
if 0:
    print(0)
elif 'spam':
    print('spam')
