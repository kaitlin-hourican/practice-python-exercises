import re

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
    pattern = r"/\w/(?P<category>.+?)/sun_"

    with open(file, "r") as images:
        for path in images:
            match = re.search(pattern, path)

            if match:
                category = match.group("category")
                if category in frequency_dict:
                    frequency_dict[category] += 1
                else:
                    frequency_dict[category] = 1
    
    for cat, freq in frequency_dict.items():
        print(f"{cat}: {freq}")


if __name__ == "__main__":
    main()