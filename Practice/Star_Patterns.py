def print_right_angle_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=' ')
        print()

def print_inverted_right_angle_triangle(rows):
    for i in range(rows, 0, -1):
        for j in range(0, i):
            print("*", end=' ')
        print()

def print_pyramid(rows):
    for i in range(0, rows):
        for j in range(0, rows - i - 1):
            print(end=" ")
        for j in range(0, i + 1):
            print("*", end=" ")
        print()

def main():
    rows = 5

    print("Right-angled Triangle:")
    print_right_angle_triangle(rows)

    print("\nInverted Right-angled Triangle:")
    print_inverted_right_angle_triangle(rows)

    print("\nPyramid:")
    print_pyramid(rows)

if __name__ == "__main__":
    main()
