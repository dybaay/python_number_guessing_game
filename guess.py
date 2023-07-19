import random


def make_guess(guess_range: int, limit: int):
    correct_number: int = random.randint(1, guess_range)
    print(correct_number)
    guess_limit: int = limit
    guess = 0
    win = False
    while guess != correct_number and guess_limit != 0 and not win:
        guess = int(input(f"Guess a number between 1 and {guess_range}: "))
        if guess > guess_range:
            print(f"{guess}, is greater than the renge of guess")

        guess_limit -= 1
        if guess > correct_number:
            print("Too high, guess again")

        if guess < correct_number:
            print("Too low, guess again")

        if guess == correct_number:
            win = True
            break

        if guess_limit > 1:
            print(f"you have {guess_limit} chances left")
        else:
            print(f"you have {guess_limit} chance left")

    if win:
        print("You win")
    else:
        print("You lose")


if __name__ == "__main__":
    make_guess(10, 3)

