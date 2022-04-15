'''
https://www.kaggle.com/code/colinmorris/strings-and-dictionaries
'''

# Strings and Dictionaries

# strings

# 1
x = 'Pluto is a planet'
y = "Pluto is a planet"
print(x == y)


# 2
print("Pluto's a planet!")
print('My dog is named "Pluto"')


# 3
print('Pluto's a planet!')


# 4
print('Pluto\'s a planet!')


# 5
hello = 'hello\nworld'
print(hello)


# 6
triplequoted_hello = """hello
world"""
print(triplequoted_hello)
print(triplequoted_hello == hello)


# 7
print('hello')
print('world')
print('hello', end='')
print('pluto', end='')


# 8
# indexing
planet = 'Pluto'
print(planet[0])


# 9
# Slicing
print(planet[-3:])


# 10
# How long is this string?
print(len(planet))


# 11
# Yes, we can even loop over them
print([char + '! ' for char in planet])


# 12
# planet.append doesn't work either
planet[0] = 'B'


# 13
# ALL CAPS
claim = 'Pluto is a planet!'
print(claim.upper())


# 14
# all lowercase
print(claim.lower())


# 15
# Searching for the first index of a substring
print(claim.index('plan'))


# 16
print(claim.startswith('planet'))


# 17
print(claim.endswith('planet!'))


# 18
words = claim.split()
print(words)


# 19
datestr = '1956-01-31'
year, month, day = datestr.split('-')
print(datestr)
print(year)
print(month)
print(day)


# 20
print('/'.join([month, day, year]))


# 21
# Yes, we can put unicode characters right in our string literals
print(' 👏 '.join([word.upper() for word in words]))


# 22
print(planet + ', we miss you.')


# 23
position = 9
print(planet + ', you will always be the ' + position + 'th planet to me.')


# 24
print(planet + ', you will always be the ' + str(position) + 'th planet to me.')


# 25
print('{}, you\'ll always be the {}th planet to me.'.format(planet, position))


# 26
pluto_mass = 1.303 * 10 ** 22
earth_mass = 5.9722 * 10 ** 24
population = 52910390
# 2 decimal points 3 decimal points format as percent separate with commas
print ('{} weights about {:.2} kilograms({:.3%} of Earth\'s mass). It is home to {:,} Plutonians'.format(
planet, pluto_mass, pluto_mass / earth_mass, population,
))


# 27
# Referring to format() arguments by index, starting from 0
s = '''Pluto\'s a {0},
No, it\'s a {1}.
{0}!
{1}! '''.format('planet', 'dwarf planet')
print(s)


# Dictionaries
# 28
numbers = {'one': 1, 'two': 2, 'three': 3}


# 29
print(numbers['one'])


# 30
numbers['eleven'] = 11
print(numbers)


# 31
numbers['one'] = 'Pluto'
print(numbers)


# 32
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)


# 33
print('Saturn' in planet_to_initial)


# 34
print('Betelgeuse' in planet_to_initial)

# 35
for k in numbers:
    print('{} = {}'.format(k,numbers[k]))


# 36
# Get all the initials, sort them alphabetically, and put them in a space-separated string
print(' '.join(sorted(planet_to_initial.values())))


# 37
for planet, initial in planet_to_initial.items():
    print('{} begins with \'{}\''.format(planet.rjust(10), initial))


# 38
help(dict)
