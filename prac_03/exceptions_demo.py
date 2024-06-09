"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? -> When non-integer values are entered.
2. When will a ZeroDivisionError occur? -> When the denominator is zero (this script avoids it).
3. Could you change the code to avoid the possibility of a ZeroDivisionError? -> Yes, by checking if the denominator is zero before division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
