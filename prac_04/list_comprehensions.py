names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# Replace the traditional for loop with a list comprehension for first initials
first_initials = [name[0] for name in names]
print(first_initials)

# Create a list containing the initials using list comprehension
full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)
# List comprehension to select names starting with 'A'
a_names = [name for name in names if name.startswith('A')]
print(a_names)
# List comprehension to convert all full names to lowercase
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)
