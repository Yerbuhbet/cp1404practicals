import random
print(dir(random))

help(random.randint)
help(random.randrange)

print("Random integer between 5 and 20:", random.randint(5, 20))  # line 1
print("Random number from range 3 to 10 step 2:", random.randrange(3, 10, 2))  # line 2
print("Random floating point number between 2.5 and 5.5:", random.uniform(2.5, 5.5))  # line 3
