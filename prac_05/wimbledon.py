import csv

# Define constants if any, like file path or specific data structures
FILENAME = "wimbledon.csv"

def main():
    data = read_data(FILENAME)
    champions, countries = process_data(data)
    display_results(champions, countries)

main()