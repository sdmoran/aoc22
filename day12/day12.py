# This is just Djikstra's/A* :)

# Read input
def read_input(fname):
    with open(fname) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]

# Convert letters to numbers
# a = 0
# Z = highest
def getHeight(letter):
    # use 64 as offset for A-Z
    if 65 <= ord(letter) and ord(letter) <= 96:
        return ord(letter) - 39 # normalize "a" to 1
    # use 96 as offset for a-z
    else:
        return ord(letter) - 97 # normalize "A" to 27

def part1(grid, start, goal):
    print(grid)
    pass

def main():

    lines = read_input("input.txt")
    start = [0, 0]
    goal = [0, 0]
    # Convert letters to numbers and also get start and goal position
    grid = []
    down = 0

    while down < len(lines):
        row = []
        across = 0
        while across < len(lines[0]):
            curr = lines[down][across]
            if curr == "S":
                start = [across, down]
                row.append(getHeight("a"))
            elif curr == "E":
                goal = [across, down]
                row.append(getHeight("z"))
            else:
                row.append(getHeight(curr))

            across += 1
        
        grid.append(row)
        down += 1

    for row in grid:
        print(row)
    # part1(lines)
    # part2(lines)

if __name__ == "__main__":
    main()