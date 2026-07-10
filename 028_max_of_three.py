def main():
    print(max_of_three(2, 7, 6))

def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == "__main_":
    main()