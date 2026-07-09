def main():
    name = input("Name: ")
    while True:
        try:
            age = int(input("Age: "))
            num = int(input("Number: "))
            if age > 0 or num > 0:
                break
        except ValueError:
            print("Please enter a valid numbers")
    
    current_year = 2026
    hundred_year = current_year + (100 - age)

    print(f"{name} will turn 100 in the year {hundred_year}\n" * num)


if __name__ == "__main__":
    main()