def main():
    get_name_frequency("nameslist.txt")
    get_category_frequency("training_01.txt")


def get_name_frequency(file):
    frequency_dict = {}

    with open(file, "r") as names:
        for name in names:
            name = name.strip()
            if name in frequency_dict:
                frequency_dict[name] += 1
            else:
                frequency_dict[name] = 1

    for name_key, count in frequency_dict.items():
        print(f"{name_key}: {count}")


def get_category_frequency(file):
    frequency_dict = {}

    with open(file, "r") as images:
        for image in images:
            category = 
            if image in frequency_dict:
                frequency_dict[image] += 1
            else:
                frequency_dict[image] = 1

    for image_ext, freq in frequency_dict.items():
        print(f"{image_ext}: {freq}")





if __name__ == "__main__":
    main()