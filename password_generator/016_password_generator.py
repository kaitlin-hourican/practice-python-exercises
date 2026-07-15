import random, string, time

def main():
    start_time = time.perf_counter()
    print("PASSWORD GENERATOR")

    type = select_type()
    length = select_length()
    special = select_chars()

    if type == "a":
        print("Password:", "".join(get_random_chars(length, special)))
    elif type == "b":
        print("Password:", generate_memorable_password(length, special))

    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Total runtime: {execution_time:.4f} seconds")


def select_type():
    while True:
        print("Password types:")
        print("  a) Gibberish (e.g. ah5if7bdmgdbuer8)")
        print("  b) Memorable (e.g. Fox754Burning)")

        type = input("Select password type: ").lower().strip()

        if type == "a":
            return type
        elif type == "b":
            return type
        else:
            print("Enter valid option")

def select_length():
    while True:
        try:
            length = int(input("Select password length (8-50): ").strip())

            if length < 8 or length > 50:
                print("Must be valid number")
            return length
        except ValueError:
            print("Must be valid number")


def select_chars():
     while True:
        special_chars = input(("Include special characters (Y/N): ")).upper().strip()

        if special_chars == "Y":
             return True
        elif special_chars == "N":
            return False
        else:
            print("Select valid option")


def generate_memorable_password(max_chars, special):
    num_words = max(1, max_chars // 10)
    word_length = 8 if max_chars >= 12 else 5

    words = []
    for _ in range(num_words):
        random_word = get_random_word(word_length).title()
        words.append(random_word)

    num_random_chars = max_chars - sum(len(word) for word in words)
    random_chars = get_random_chars(num_random_chars, special)

    return "".join(words + random_chars)


def get_random_word(max_chars):
    with open("sowpods.txt") as file:
        words = [line.strip() for line in file.readlines()]
        valid_words = [word for word in words if len(word) <= max_chars]
        return random.choice(valid_words)
    
def get_random_chars(num, special):
    special_pool = string.ascii_letters + string.digits + string.punctuation
    alphanum_pool = string.ascii_letters + string.digits 
    chars = special_pool if special else alphanum_pool

    return random.choices(chars, k=num)


if __name__ == "__main__":
    main()