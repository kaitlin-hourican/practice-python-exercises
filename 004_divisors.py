def main():
    while True:
        try:
            num = int(input("Number: "))
            break
        except ValueError:
            print("Enter a valid number")

    print(f"Divisors of {num}:", divisors(num))


def divisors(num):
    i = 1
    divisor_list = []

    while i <= num:
        if num % i == 0:
            divisor_list.append(i)
        i += 1
    
    return divisor_list



if __name__ == "__main__":
    main()