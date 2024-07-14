"""CP1404/CP5632 Practical - Guitar program."""

from prac_06.guitar import Guitar

def main():
    """Manage a collection of guitars."""
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("\nName: ")

if __name__ == '__main__':
    main()
