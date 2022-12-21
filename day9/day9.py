import copy

# Read input
def read_input(fname):
    with open(fname) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]

def manhattanDistance(headPos, tailPos):
    return abs(headPos[0] - tailPos[0]) + abs(headPos[1] - tailPos[1])

# True if same column False otherwise
def isInSameColumn(headPos, tailPos):
    return headPos[0] == tailPos[0] or headPos[1] == tailPos[1]

# should move if:
# - in same column, and distance > 1
# - in different column, and distance > 2
def shouldMove(headPos, tailPos):
    dist = manhattanDistance(headPos, tailPos)
    if isInSameColumn(headPos, tailPos):
        return dist > 1
    else:
        return dist > 2

# In all cases, tail just follows head if it needs to move... no need to do check positions
def getTailMove(headPos, tailPos, prevHeadPos, tailMoves):
    if shouldMove(headPos, tailPos):
        tailPos[0] = prevHeadPos[0]
        tailPos[1] = prevHeadPos[1]

    tailStr = f"{tailPos[0]};{tailPos[1]}"
    if tailStr not in tailMoves:
        tailMoves.add(tailStr)

def part1(lines):
    tailMoves = set()

    headPos = [0, 0]
    prevHeadPos = [0, 0]
    tailPos = [0, 0]

    for line in lines:
        # get moves for head
        direction = line[0]
        dist = int(line[2:])
        
        dirCoords = [0, 0] # direction as a vector

        # move head
        if direction == "R":
            # move right (+X)
            dirCoords = [1, 0]
        if direction == "L":
            # move left (-X)
            dirCoords = [-1, 0]
        if direction == "U":
            # move up (+Y)
            dirCoords = [0, 1]
        if direction == "D":
            # move down (-Y)
            dirCoords = [0, -1]

        for _ in range(dist):
            prevHeadPos[0] = headPos[0]
            prevHeadPos[1] = headPos[1]
            headPos[0] += dirCoords[0]
            headPos[1] += dirCoords[1]
            getTailMove(headPos, tailPos, prevHeadPos, tailMoves)
        
    
    print(f"Tail moves: {len(tailMoves)}, headPos: {headPos}, tailPos: {tailPos}")

    for Y in range(25):
        for X in range(20):
            if f"{X};{24-Y}" in tailMoves:
                print("#", end="")
            else:
                print(".", end="")
        print("\n")


# TODO finish this - if I end up with willpower and time later on :)
def part2(lines, size):
    tailMoves = set()
    ropePos = []
    for _ in range(size):
        ropePos.append([0, 0])
    head = ropePos[0] # head is ropePos[0]
    print(ropePos)
    # longer rope; len 10.
    # When tail needs to move, REST of rope ALSO needs to move - following tail like tail follows head.
    # so pos of rope[i] = rope(i - 1)
    # then check last index of rope and add to set if needed.

    for line in lines:
        # get moves for head
        direction = line[0]
        dist = int(line[2:])
        
        dirCoords = [0, 0] # direction as a vector

        # move head
        if direction == "R":
            # move right (+X)
            dirCoords = [1, 0]
        if direction == "L":
            # move left (-X)
            dirCoords = [-1, 0]
        if direction == "U":
            # move up (+Y)
            dirCoords = [0, 1]
        if direction == "D":
            # move down (-Y)
            dirCoords = [0, -1]

        for _ in range(dist):
            head[0] += dirCoords[0]
            head[1] += dirCoords[1]
            moveRope()

        print(ropePos)

    pass

def main():
    lines = read_input("input.txt")
    # part1(lines)
    part2(lines, 10)

if __name__ == "__main__":
    main()