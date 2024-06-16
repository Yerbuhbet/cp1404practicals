"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

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
        parts[2] = int(parts[2])
        data.append(parts)
    input_file.close()
    return data

def display_subjects(data):
    """Display the details of each subject from the provided data."""
    print("\nSubject Details\n----------------")
    for subject_details in data:
        subject_code, lecturer, student_count = subject_details
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")

main()
