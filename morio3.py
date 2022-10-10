def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        square_row(size)

def square_row(width):
    print("#" * width)

main()