# Read the puzzle here: https://adventofcode.com/2024/day/1

def main():
    # Open the input file and read all lines
    with open("input.txt", "r") as input:
        lines = input.read().splitlines()

    # Initialize lists to store the left and right values
    left = []
    right = []

    # Split each line into two values and append to respective lists
    for line in lines:
        x, y = line.split()
        left.append(int(x))
        right.append(int(y))

    # Holds the total as it is being calculatted
    distance = 0

    # Calculate the total distance by summing the absolute differences
    # between corresponding sorted elements of left and right lists
    for x, y in zip(sorted(left), sorted(right)):
        distance += abs(x - y)

    print(distance)


if __name__ == '__main__':
    main()