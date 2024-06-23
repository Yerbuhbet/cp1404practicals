def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)  # Commit 2
        confirmation = input(f"Is your name {name}? (Y/n) ")  # Commit 3
        if confirmation.lower() not in ('y', 'yes', ''):
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():  # Commit 4
        print(f"{name} ({email})")

def get_name_from_email(email):  # Commit 2
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name

main()
