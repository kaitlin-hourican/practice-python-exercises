def main():
    while True:
        try:
            word = input("Give me a word: ").replace(" ", "").lower()
            if word.isalpha():
                break
        except ValueError:
            print("Input cannot contains numbers or punctuation")

    if is_palindrome(word):
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")
    

def is_palindrome(word):
    return word == word[::-1]

if __name__ == "__main__":
    main()

    