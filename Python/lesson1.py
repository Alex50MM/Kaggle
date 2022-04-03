'''
https://www.kaggle.com/code/colinmorris/hello-python
'''

# Hello, Python
# 1
spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon, and Spam (4 more serving of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But i don't want ANY spam!")

viking_song = 'Spam ' * spam_amount
print (viking_song)

# 2
spam_amount = 0

# 3
print(spam_amount)

# 4
# Ordering Spam, egg, Spam, Spam, bacom and Spam (4 more serving of Spam)
spam_amount = spam_amount + 4

# 5
if spam_amount > 0:
    print("But i don't want ANY spam!")

viking_song = 'Spam Spam Spam'
print(viking_song)

# 6
viking_song = 'Spam ' * spam_amount
print(viking_song)

# 7
spam_amount = 0

# 8
type(spam_amount)
print(type(spam_amount))

# 9
type(19.95)
print(type(19.95))

# 10
print(5 / 2)
print(6 / 2)

# 11
print(5 // 2)
print(6 // 2)

# 12
8 - 3 + 2
print(8 - 3 + 2)

# 13
-3 + 4 * 2
print(-3 + 4 * 2)

# 14
hat_height_cm = 25
my_height_cm = 190
# How tall am I, in meters, when wearing my hat?
total_height_meters = hat_height_cm + my_height_cm / 100
print('Height in meters = ', total_height_meters, "?")

# 15
total_height_meters = (hat_height_cm + my_height_cm) / 100
print('Height in meters = ', total_height_meters)

# 16
print(min(1, 2, 3))
print(max(1, 2, 3))

# 17
print(abs(32))
print(abs(-32))

# 18
print(float(10))
print(int(3.33))
# They can even be called on strings!
print(int('807') + 1)
