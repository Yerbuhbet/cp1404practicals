"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting.
(We prefer f-strings in this subject.)
Want to read more about it?
https://docs.python.org/3/library/string.html#formatstrings
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

# The 'old' manual way to format text with string concatenation (don't do this):
print("My guitar: " + name + ", first made in " + str(year))
