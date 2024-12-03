# Read the puzzle here: https://adventofcode.com/2024/day/1#part2

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

    # Holds the similarity score as it is being calculated
    similarity = 0

    # Calculate the similarity score by looping over the left numbers
    for number in left:
        # and adding to the similarity the number
        # multiplied by the times it appears on the right
        similarity += number * right.count(number)

    print(similarity)

if __name__ == '__main__':
    main()