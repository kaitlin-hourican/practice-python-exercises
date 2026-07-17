import random  


def main():
    number = generate_random_number()
    guess_count = 0

    print("Welcome to the Cows and Bulls Game!")
    print("Enter a 4-digit number: ")
    while True:
        try:
            guess_str = list(input(">>> ").strip())

            if len(guess_str) != 4:
                print("Please enter exactly 4 digits.")
                continue

            guess = [int(x) for x in guess_str]

            cows, bulls = is_correct(number, guess)
            guess_count += 1

            print(f"{cows} cows, {bulls} bulls.")
            if cows == 4:
                print(f"You won in {guess_count} guesses.")
                break

        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue


def generate_random_number():
    number = []

    while len(number) < 4:
        num = random.randint(0, 9)
        if num not in number:
            number.append(num)
    return number


def is_correct(number, guess):
    cow_count = 0
    bull_count = 0

    number_copy = list(number)
    guess_copy = list(guess)

    for i in range(4):
        if guess[i] == number[i]:
            cow_count += 1
            number_copy[i] = None
            guess_copy[i] = None

    for i in range(4):
        if guess_copy[i] is not None and guess_copy[i] in number_copy:
            bull_count += 1
            number_copy[number_copy.index(guess_copy[i])] = None

    return (cow_count, bull_count)


if __name__ == "__main__":
    main()