import random

BASIC_LEVEL_ATTEMPTS = 10
CORE_LEVEL_ATTEMPTS = 5



def set_difficulty(level_chosen):
    if level_chosen == 'easy':
        return BASIC_LEVEL_ATTEMPTS
    elif level_chosen == 'hard':
        return CORE_LEVEL_ATTEMPTS
    else:
        print("Invalid level choice. Please choose 'easy' or 'hard'.")
        return None


def check_answer(guessed_number, answer, attempts):
    if guessed_number < answer:
        print("The guessed number is too small.")
        return attempts - 1
    elif guessed_number > answer:
        print("The guessed number is too high.")
        return attempts - 1
    else:
        print(f"You guessed the right number! The answer is {answer}.")
        return 0


def game():
    print("Let me think of a number between 1 and 100.")
    answer = random.randint(1, 100)
    level = input("Choose a level: Type 'easy' or 'hard': ").lower()
    attempts = set_difficulty(level)

    if attempts is None:
        return

    guessed_number = 0
    while guessed_number != answer and attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number:")
        guessed_number = int(input("Guess the number: "))
        attempts = check_answer(guessed_number, answer, attempts)
        if attempts == 0 and guessed_number != answer:
            print("You are out of guesses. You lose!")
            return
        elif guessed_number != answer:
            print("Guess again!")


game()
