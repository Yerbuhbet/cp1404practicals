import random  # Import the random module to access its functions.

# Using dir() to inspect the contents of the random module.
# This will list all attributes, methods, and functions available in the 'random' module.
print(dir(random))

# Exploring specific functions within the 'random' module using help().
# This provides details on how to use the functions and what parameters they accept.
help(random.randint)  # Shows help on the randint() function which returns an integer between the provided bounds.
help(random.randrange)  # Shows help on the randrange() function which returns a randomly selected element from the specified range.

# Demonstrating the use of random.randint() which includes both endpoints.
print("Random integer between 5 and 20:", random.randint(5, 20))  # line 1

# Demonstrating the use of random.randrange() which is like range() and does not include the endpoint.
print("Random number from range 3 to 10 step 2:", random.randrange(3, 10, 2))  # line 2

# Demonstrating the use of random.uniform() which returns a floating-point number.
print("Random floating point number between 2.5 and 5.5:", random.uniform(2.5, 5.5))  # line 3

# Answers to questions for learning purposes:
# What did you see on line 1?
# Answer: A random integer between 5 and 20. The smallest possible number is 5 and the largest is 20.

# What did you see on line 2?
# Answer: A random number from the sequence 3, 5, 7, 9. The smallest number could be 3 and the largest 9.
# Could line 2 have produced a 4? Answer: No, because 4 is not in the sequence generated by range(3, 10, 2).

# What did you see on line 3?
# Answer: A random floating-point number between 2.5 and 5.5. The smallest could be just above 2.5 and the largest just below 5.5.

# Code to produce a random number between 1 and 100 inclusive:
random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")
