# Setup empty function structures for file operations

def write_name():
    out_file = open("name.txt", "w")
    name = input("What is your name? ")
    print(name, file=out_file)
    out_file.close()


def read_name():
    pass

def read_name_with():
    pass

def sum_first_two_numbers():
    pass

def sum_all_numbers():
    pass

def main():
    pass

main()
