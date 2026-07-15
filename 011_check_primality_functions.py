def main():

    while True:
        try:
            num = int(input("Give me a number: "))

            if num < 1:
                print("Must be positive number")
                continue
            break
        except ValueError:
            print("Enter a valid number")

    num_prime = is_prime(num)

    if num_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

def is_prime(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True

if __name__ == "__main__":
    main()