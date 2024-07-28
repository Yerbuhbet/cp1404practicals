import csv
from guitar import Guitar


def main():
    """Main program to read, display, sort, and add guitars."""
    guitars = load_guitars("guitars.csv")
    display_guitars(guitars)

    # Sort the guitars by year (oldest to newest) and display them
    guitars.sort()
    print("\nGuitars sorted by year (oldest to newest):")
    display_guitars(guitars)

    # Add new guitars from user input
    guitars += get_new_guitars()

    # Write all guitars back to the file
    save_guitars("guitars.csv", guitars)


def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """Display a list of guitars."""
    for guitar in guitars:
        print(guitar)


def get_new_guitars():
    """Get new guitars from the user."""
    guitars = []
    print("\nEnter your new guitars (leave name empty to finish):")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
    return guitars


def save_guitars(filename, guitars):
    """Save guitars to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


if __name__ == "__main__":
    main()
