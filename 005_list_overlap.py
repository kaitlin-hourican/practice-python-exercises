def get_list_overlap(a, b):
    overlap = []
    for el in a:
        if el in b and el not in overlap:
            overlap.append(el)

    return overlap

list_1 = [ 1, 2, 3, 4, 5, 6, 7, 8]
list_2 = [ 2, 4, 6, 8]
list_3 = [ 1, 3, 3, 5, 7, 9, 10, 15]
list_4 = [ 4, 4.5, -2, 10, 1, 4]

print(get_list_overlap(list_2, list_1))
print(get_list_overlap(list_2, list_4))
print(get_list_overlap(list_3, list_4))
print(get_list_overlap(list_1, list_3))

