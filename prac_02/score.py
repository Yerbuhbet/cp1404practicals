import random

def main():
    user_score = float(input("Enter your score: "))
    print(evaluate_score(user_score))
    random_score = random.randint(0, 100)
    print(f"Random score evaluation: {random_score} is {evaluate_score(random_score)}")

