'''
https://www.kaggle.com/code/colinmorris/lists
'''

# Lists

# 1
primes = [2, 3, 5, 7]


# 2
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']


# 3
hands = [
         ['J', 'Q', 'K'],
         ['2', '2', '2'],
         ['6', 'A', 'K'], # comma (,) after the last element is optional
]

# I could also have written this on one line, but it can get hard to read
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]


# 4
my_favourite_things = [32, 'raindrops on roses', help]


# 5

print(planets)
print(planets[0])


# 6
print(planets[1])


# 7
print(planets[-1])


# 8
print(planets[-2])


# 9
print(planets[0: 3])


# 10
print(planets[:3])


# 11
print(planets[3:])


# 12
# All the planets except the first and last
print(planets[1: -1])


# 13
# The last 3 planets
print(planets[-3:])


# 14
planets[3] = 'Malacandra'
print(planets)


# 15
planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
# Let's give them back their old names
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars']


# 16
# How many planets are there?
print(len(planets))


# 17
# The planets sorted in alphabetical order
print(sorted(planets))


# 18
primes = [2, 3, 5, 7]
print(sum(primes))


# 19
print(max(primes))


# 20
x = 12
# x is a real number, so it's imaginary part is 0
print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag)


# 21
print(x.bit_length)


# 22
print(x.bit_length())


# 23
help(x.bit_length)


# 24
# Pluto is a planet darn it!
planets.append('Pluto')
print(planets)


# 25
help(planets.append)


# 26
print(planets)


# 27
planets.pop()


# 28
print(planets)


# 29
print(planets.index('Earth'))


# 30
print(planets.index('Pluto'))


# 31
print('Earth' in planets)


# 32
print('Calbefraques' in planets)


# 33
help(planets)


# 34
t = (1, 2, 3)


# 35
t = 1, 2, 3
print(t)


# 36
t[0] = 100


# 37
x = 0.125
print(x.as_integer_ratio())


# 38
numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)


# 39
a = 1
b = 0
a, b = b, a
print(a, b)
