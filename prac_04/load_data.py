def main():
    data = load_data()
    display_subjects(data)
def load_data():
    """Read data from file and return a list of lists containing subject, lecturer, and student count."""
    data = []
    input_file = open(FILENAME, 'r')
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])  # Convert student count from string to int
        data.append(parts)  # Append the list of parts to the data list
    input_file.close()
    return data
