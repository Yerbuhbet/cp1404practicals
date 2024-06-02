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