'''
https://www.kaggle.com/code/colinmorris/working-with-external-libraries
'''

# Working with External Libraries

# imports

# 1
import math
print('It\'s math! It has type {}'.format(type(math)))


# 2
print(dir(math))


# 3
print('Pi to 4 significant digits = {:.4}'.format(math.pi))


# 4
print(math.log(32, 2))


# 5
print(help(math.log))


# 6
print(help(math))


# 7
import math as mt
print(mt.pi)


# 8
import math
mt = math


# 9
from math import *
print(pi, log(32, 2))


# 10
from math import *
from numpy import *
#print(pi, log(32, 2))


# 11
from math import log, pi
from numpy import asarray


# 12
import numpy
print('numpy.random is a', type(numpy.random))
print('is contains names such as...',
      dir(numpy.random)[-15:]
      )


# 13
# Roll 10 dice
rolls = numpy.random.randint(low = 1, high = 6, size = 10)
print(rolls)


# 14
print(type(rolls))


# 15
print(dir(rolls))


# 16
print(rolls.mean())


# 17
print(rolls.tolist())


# 18
print(help(rolls.ravel))


# 19
#print(help(rolls))


# 20
[3, 4, 1, 2, 2, 1] + 10


# 21
print(rolls + 10)


# 22
print(rolls)
print(rolls <= 3)


# 23
xlist = [[1, 2, 3], [2, 4, 6], ]
# Create a 2-Dimensional array
x = numpy.asarray(xlist)
print('xlist = {}\nx = \n{}'.format(xlist, x))


# 24
print(x[1, -1])


# 25
# Get the last element of the second sublist of our nested list
print(xlist[1, -1])


# 26

import tensorflow as tf
# Create two constants, each with value 1
a = tf.constant(1)
b = tf.constant(1)
# Add together to get
print(a + b)


# 27
print(dir(list))
