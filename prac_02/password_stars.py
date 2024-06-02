MIN_LENGTH = 8
def main():
    password = get_password(MIN_LENGTH)
    print('*' * len(password))

def get_password(MIN_LENGTH):
    password = input("Enter your password: ")
    if len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long. Please try again.")
        return get_password(MIN_LENGTH)
    return password
