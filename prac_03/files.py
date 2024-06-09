# Quick Program 1
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)  # or out_file.write(name)
out_file.close()
# Quick Program 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)
# Quick Program 2 using "with"
with open("name.txt", "r") as in_file:
    name = in_file.read().strip()
print("Your name is", name)
