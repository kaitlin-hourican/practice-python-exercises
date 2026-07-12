def main():
    while True:
        try:
            length = int(input("Number of fibonacci numbers: "))
            if length > 0:
                break
            print("Enter a number larger than 0")
        except ValueError:
            print("Enter a valid number")

    print(fibonacci(length))

def fibonacci(length):
    fib_seed = [1, 1]

    if length == 1:
        return [1]
    if length == 2:
        return fib_seed
    
    i = 1
    while len(fib_seed) < length:
        next_num = fib_seed[i] + fib_seed[i - 1]
        fib_seed.append(next_num)
        i += 1
    
    return fib_seed

if __name__ == "__main__":
    main()