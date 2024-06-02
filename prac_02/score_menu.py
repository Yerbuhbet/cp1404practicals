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