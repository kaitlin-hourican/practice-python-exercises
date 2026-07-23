def main():
    prime_list = file_to_list("primenumbers.txt")
    happy_list = file_to_list("happynumbers.txt")

    overlap_list = [num for num in prime_list if num in happy_list]
    print(overlap_list)

    
def file_to_list(file):
    file_list = []

    with open(file) as f:
        line = f.readline()
        while line:
            file_list.append(int(line))
            line = f.readline()

    return file_list


if __name__ == "__main__":
    main()