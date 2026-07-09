def main():
    while True:
        try:
            num = int(input("First number: "))
            check = int(input("Second number: "))
            break
        except ValueError:
            print("Enter a valid number")

    if num % 2 == 0:
        print("Multiple of 4" if num % 4 == 0 else "Even")
    else:
        print("Odd")

    print(f"Divided by {check}" if num % check == 0 else f"Not divided by {check}")
    

if __name__ == "__main__":
    main()