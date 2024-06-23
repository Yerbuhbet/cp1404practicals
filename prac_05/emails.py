def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        email = input("Email: ")
def get_name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name
