def main():

    while True:
        words = input("Give me a sentence: ")

        if " " not in words:
            print("Please provide words separated by space")
        else:
            break
    
    reversed = reverse_words(words)

    print(reversed)


def reverse_words(words):
    word_list = words.split(" ")
    return " ".join(word_list[::-1])


if __name__ == "__main__":
    main()