def main():
    score = get_valid_score()
    choice = display_menu()
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print(f"The result is: {evaluate_score(score)}")
        elif choice == 'S':
            print("*" * int(score))
        else:
            print("Invalid option")
        choice = display_menu()
def get_valid_score():
    score = float(input("Enter a valid score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. The score must be between 0 and 100.")
        score = float(input("Enter a valid score (0-100): "))
    return score

def evaluate_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def display_menu():
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")
    return input("Enter your choice: ").upper()

main()