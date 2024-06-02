def main():
    password = get_password()
    print_asterisks(password)

def get_password():
    min_length = 8
    password = input("Enter your password: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long.")
        password = input("Enter your password: ")
    return password