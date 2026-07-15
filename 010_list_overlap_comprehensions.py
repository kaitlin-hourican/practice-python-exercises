import random

def main():
    list_a = get_random_list()
    list_b = get_random_list()

    print(list_a)
    print(list_b)
    print(get_duplicates(list_a, list_b))


def get_duplicates(list_a, list_b):
    set_a = set(list_a)
    set_b = set(list_b)
    return [num for num in list_a if num in set_b]

def get_random_list():
    length = random.randint(0, 50)
    return [random.randint(0, 100) for _ in range(length)]


if __name__ == "__main__":
    main()