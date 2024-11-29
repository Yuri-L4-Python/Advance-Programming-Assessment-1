import random

def get_difficulty_level():
    print("DIFFICULTY LEVEL\n1. Easy\n2. Moderate\n3. Advanced")
    while True:
        try:
            level = int(input("Select difficulty level (1-3): "))
            if level in [1, 2, 3]:
                return level
            print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_random_number(level):
    ranges = {1: (1, 9), 2: (10, 99), 3: (1000, 9999)}
    return random.randint(*ranges[level])

def display_problem(num1, num2, operation):
    try:
        return int(input(f"{num1} {operation} {num2} = "))
    except ValueError:
        return None

def calculate_score(attempt, correct):
    return 10 if attempt == 1 and correct else 5 if attempt == 2 and correct else 0

def display_results(score):
    print(f"\nQuiz Finished! Your final score: {score}/100")
    ranks = [(90, "A+"), (80, "A"), (70, "B"), (60, "C")]
    for threshold, rank in ranks:
        if score > threshold:
            print(f"Rank: {rank}")
            break
    else:
        print("Rank: F")

def math_quiz():
    while True:
        difficulty = get_difficulty_level()
        score = 0

        for _ in range(10):
            num1, num2 = generate_random_number(difficulty), generate_random_number(difficulty)
            operation = random.choice(["+", "-"])
            if operation == "-" and num1 < num2:
                num1, num2 = num2, num1
            correct_answer = num1 + num2 if operation == "+" else num1 - num2

            for attempt in range(1, 3):
                user_answer = display_problem(num1, num2, operation)
                if user_answer == correct_answer:
                    print("Correct!")
                    score += calculate_score(attempt, True)
                    break
                elif attempt == 1:
                    print("Incorrect. Try again.")
                else:
                    print(f"Wrong. The correct answer was {correct_answer}.")

        display_results(score)
        if input("Do you want to play again? (yes/no): ").strip().lower() != "yes":
            print("Thank you for playing!")
            break

math_quiz()
