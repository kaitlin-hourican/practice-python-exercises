import random

def main():
    print(random_word())
    print(random_word())
    print(random_word())

def random_word():
    with open("sowpods.txt") as file:
        words = file.readlines()
        return random.choice(words)


if __name__ == "__main__":
    main()