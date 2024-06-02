MIN_LENGTH = 8
def main():
    password = get_password(MIN_LENGTH)
    print('*' * len(password))

def get_password(MIN_LENGTH):
    password = input("Enter your password: ")