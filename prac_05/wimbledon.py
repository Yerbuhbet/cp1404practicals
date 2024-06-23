import csv

# Define constants if any, like file path or specific data structures
FILENAME = "wimbledon.csv"

def main():
    data = read_data(FILENAME)
    champions, countries = process_data(data)
    display_results(champions, countries)

def read_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader)  
        data = [line for line in reader]
    return data


main()