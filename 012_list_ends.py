def main():
    nums = [1, 2, 4, 5, 7, 9, 13]

    bookends = bookend_list(nums)

    print(bookends)

def bookend_list(full_list):
    short_list = [full_list[0], full_list[len(full_list) - 1]]

    return short_list

if __name__ == "__main__":
    main()