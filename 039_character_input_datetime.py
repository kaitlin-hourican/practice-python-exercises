from datetime import date

def main():
    while True:
        try:
            name = input("Name: ")
            age = int(input("Age (years): "))
            break
        except ValueError:
            print("Enter a valid name and age")
    
    print(f"{name} will turn 100 in the year {hundredth_year(age)}")


def hundredth_year(age):
    current_year = date.today().year
    return current_year - age + 100


if __name__ == "__main__":
    main()