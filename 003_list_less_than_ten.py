def main():
    while True:
        try:
            max = int(input("Enter a max number: "))
            break
        except ValueError:
            print("Max must be a number")

    print(list_filter([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]))
    print(list_filter([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], max))
    
def list_filter(nums, max = 5):
    return [num for num in nums if num < max]


if __name__ == "__main__":
    main()

