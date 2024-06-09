"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main():
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)} character password is valid: {password}")

def is_valid_password(password):
    if not MIN_LENGTH <= len(password) <= MAX_LENGTH:
        return False

    number_of_lower = sum(1 for c in password if c.islower())
    number_of_upper = sum(1 for c in password if c.isupper())
    number_of_digit = sum(1 for c in password if c.isdigit())
    number_of_special = sum(1 for c in password if c in SPECIAL_CHARACTERS)

    if number_of_lower == 0 or number_of_upper == 0 or number_of_digit == 0:
        return False
    if IS_SPECIAL_CHARACTER_REQUIRED and number_of_special == 0:
        return False

    return True


main()
