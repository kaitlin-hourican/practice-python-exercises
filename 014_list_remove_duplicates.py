def main():
    print(remove_duplicates_loop([11, 2, 15, 16, 25 , 3, 5, 2, 6, 22, 16]))
    print(remove_duplicates_sets([11, 2, 15, 16, 25 , 3, 5, 2, 6, 22, 16]))


def remove_duplicates_loop(elements):
    unqiue_list = []

    for el in elements:
        if el not in unqiue_list:
            unqiue_list.append(el)
        
    return unqiue_list


def remove_duplicates_sets(elements):
    unique_elements = set(elements)

    return list(unique_elements)

if __name__ == "__main__":
    main()