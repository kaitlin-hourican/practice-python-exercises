import random

def main():
    print(get_list_overlap(random_list(), random_list()))
    print(get_list_overlap(random_list(), random_list()))
    print(get_list_overlap(random_list(), random_list()))

def get_list_overlap(a, b):
    overlap = []
    for el in a:
        if el in b and el not in overlap:
            overlap.append(el)

    return overlap

def random_list():
    return random.choices(range(1, 51), k=random.randint(1, 25))

if __name__ == "__main__":
    main()