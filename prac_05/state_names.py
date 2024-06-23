"""
CP1404/CP5632 Practical
State names in a dictionary
"""

CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}
def main():
    """Get user state input and print the full state name."""
    print_state_names()  # Display all states at the start
    state_code = input("Enter short state: ").upper()
    while state_code != "":
        try:
            print(f"{state_code} is {CODE_TO_NAME[state_code]}")
        except KeyError:
            print("Invalid short state")
        state_code = input("Enter short state: ").upper()

def print_state_names():
    """Print all state abbreviations and their full names."""
    for code, name in CODE_TO_NAME.items():
        print(f"{code} is {name}")



main()
