"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

def main():
     """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))
    for month in range(1, months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
