def main():
    while True:
        try:
            board_size = int(input("Enter board game size: "))
            if board_size > 2:
                break
            print("Must be size 3 minimum")
        except ValueError:
            print("Enter a number")
    
    assemble_board(board_size)
    

def print_horizontals(size):
    print(" " + "--- " * size)


def print_verticals(size):
    print("|   " * (size + 1)) 


def assemble_board(size):
    i = 0
    while i < size:
        print_horizontals(size)
        print_verticals(size)
        i += 1

    print_horizontals(size)

if __name__ == "__main__":
    main()