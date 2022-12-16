# Read input
def read_input(fname):
    with open(fname) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]

# Get starting state
def getStacks(lines):
    # Quick and hacky. Lots of assumptions here :)

    stacks = []
    for i in range(9):
        stacks.append([])

    # Initial state provided in lines 0-8; line 9 just gives stack numbers
    for line in reversed(lines[:8]):
        # Each input container is constant position in line; 1, 5, 9, etc.
        for i in range(9):
            if (i * 4 + 1) < len(line):
                c = line[i * 4 + 1]
                if c != " ":
                    stacks[i].append(c)
    print(stacks)
    return stacks

# Get list of tuple (move #, fromStack, toStack)
def getMoves(lines):
    moves = []
    for line in lines:
        split = line.split(" ")
        count, src, dest = split[1], split[3], split[5]
        moves.append((int(count), int(src), int(dest)))
    return moves

# Move x containers from src stack to dest stack
def move(state, x, src, dest):
    for _ in range(x):
        state[dest].append(state[src].pop())

# pop multiple items in-order from src stack
def popMany(src, dest, x):
    items = []
    for i in reversed(range(x)):
        items.append(src[len(src) - 1 - i])
    for i in range(x):
        src.pop()
    return (src, items)


# Move x containers from src stack to dest stack, ALL AT ONCE - don't pop individually every time
def moveMany(state, x, src, dest):
    print("Moving ", x)
    print("From", state[src])
    print("to", state[dest])

    for i in reversed(range(x)):
        state[dest].append(state[src][len(state[src]) - 1 - i])
    for i in range(x):
        state[src].pop()

def part1(stacks, moves):
    for m in moves:
        move(stacks, m[0], m[1] - 1, m[2] - 1)

def part2(stacks, moves):
    for m in moves:
        print(stacks)
        moveMany(stacks, m[0], m[1] - 1, m[2] - 1)
    for stack in stacks:
        print(stack[-1])
    print(stacks)
    

def main():
    lines = read_input("input.txt")

    stacks = getStacks(lines)
    moves = getMoves(lines[10:])
    print(part1(stacks, moves))
    stacks = getStacks(lines)
    print(part2(stacks, moves))




if __name__ == "__main__":
    main()