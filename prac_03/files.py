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
