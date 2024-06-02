import random

def main():
    user_score = float(input("Enter your score: "))
    print(evaluate_score(user_score))
    random_score = random.randint(0, 100)
    print(f"Random score evaluation: {random_score} is {evaluate_score(random_score)}")

def evaluate_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"