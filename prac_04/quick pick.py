import random

# Constants for the lottery configuration
NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45
def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in sorted(quick_pick)))
