# Read input
def read_input(fname):
    with open(fname) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]

# Feels like these methods could all be refactored to be 1-2 instead of 4.
# Each returns tuple (bool visible, int distance)
# visible indicates if this tree is visible or not.
# distance indicates how many trees away the block occurs (if no block, the distance to edge.)
def distLeft(grid, across, down):
    # trees to left (same down, decreasing across)
    dist = 1
    while across - dist > 0: # for part1, >. For part2, >!
        if int(grid[down][across - dist]) >= int(grid[down][across]):
            return (False, dist)
        dist += 1
    return (True, dist)
 
def distRight(grid, across, down):
    # trees to right (same down, increasing across)
    dist = 1
    while across + dist < len(grid[0]):
        if int(grid[down][across + dist]) >= int(grid[down][across]):
            return (False, dist)
        dist += 1
    return (True, dist - 1) # account for extra addition to dist


def distUp(grid, across, down):
    # trees above (same across, decreasing down)
    dist = 1
    while down - dist > 0: # for part1, >. For part2, >!
        if int(grid[down - dist][across]) >= int(grid[down][across]):
            return (False, dist)
        dist += 1
    return (True, dist)
    
def distDown(grid, across, down):
    # trees above (same across, increasing down)
    dist = 1
    while down + dist < len(grid):
        if int(grid[down + dist][across]) >= int(grid[down][across]):
            return (False, dist)
        dist += 1
    return (True, dist - 1) # account for extra addition to dist

# a tree is visible if...
# - it is on an edge
# - it is taller than all trees in any direction
# - (not implemented, but would make things much faster) its neighbors are visible AND it is taller than its neighbors
def isVisible(grid, x, y):
    # on the edge
    if x == 0 or y == 0 or x == len(grid[0]) - 1 or y == len(grid) - 1:
        return True

    # trees in ANY direction are shorter
    return distLeft(grid, x, y)[0] or distRight(grid, x, y)[0] or distUp(grid, x, y)[0] or distDown(grid, x, y)[0]

def getViewDistance(grid, down, across):
    # ViewDistance is distance to each edge or closest blocking tree multiplied. Trees on edge are 0.
    if across == 0 or down == 0 or across == len(grid[0]) - 1 or down == len(grid) - 1:
        return 0
        
    dists = [distLeft(grid, across, down)[1], distRight(grid, across, down)[1], distUp(grid, across, down)[1], distDown(grid, across, down)[1]]
    score = dists[0] * dists[1] * dists[2] * dists[3] 
    # print(f"Dists for {grid[down][across]} at {across} across, {down} down: LEFT {dists[0]}, RIGHT {dists[1]}, UP {dists[2]}, DOWN {dists[3]} = {score}")
    return score 
 
def part1(lines):
    count = 0
    for down in range(len(lines)): # down
        for across in range(len(lines[0])): # across
            if isVisible(lines, down, across):
                count += 1
    print("COUNT: ", count)

def part2(lines):
    bestView = 0

    for down in range(len(lines)):
        for across in range(len(lines[0])):
            bestView = max(bestView, getViewDistance(lines, down, across))
    print("BEST VIEW: ", bestView)


def main():
    lines = read_input("input.txt")
    part1(lines)
    part2(lines)

if __name__ == "__main__":
    main()