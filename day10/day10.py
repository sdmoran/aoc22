# Read input
def read_input(fname):
    with open(fname) as f:
        lines = f.readlines()
        return [line.lstrip("\t").rstrip() for line in lines]

interestedLines = [20, 60, 100, 140, 180, 220] # could also do 20 + 40*i or whatever

def part1(lines):
    x = 1

    signalSum = 0

    lineNum = 0
    cycleNum = 0
    while lineNum < len(lines):
        line = lines[lineNum]
        cycleNum += 1
        # print(f"Before Cycle #{cycleNum}, x = {x}")
        if cycleNum % 20 == 0 and cycleNum in interestedLines:
            signalSum += cycleNum * x
            print(f"After cycle {cycleNum}: x = {x}")
        if "addx" in line:
            cycleNum += 1
            if cycleNum % 20 == 0 and cycleNum in interestedLines:
                signalSum += cycleNum * x
                print(f"After cycle {cycleNum}: x = {x}")
            x += int(line[5:])
        # print(f"After Cycle #{cycleNum}, x = {x}")
        # print(line)
        lineNum += 1
    print("SUM: ", signalSum)

def draw(cycleNum, middlePos):
    if abs(cycleNum % 40 - 1 - middlePos) <= 1:
        print("#", end="")
    else:
        print(".", end="")
    if cycleNum % 40 == 0:
        print("")


def part2(lines):
    x = 1

    cycle = 0
    lineNum = 0
    adding = False

    while lineNum < len(lines):
        line = lines[lineNum]
        cycle += 1 # always tick cycle

        draw(cycle, x)
        # if noop, advance immediately
        if "noop" in line:
            lineNum += 1

        # if addx
        else:
            # if first time seen, mark as such and do not yet advance
            if not adding:
                adding = True
            # if 2nd time seen, mark as such, advance, and add
            else:
                lineNum += 1
                adding = False
                x += int(line[5:])



def main():
    lines = read_input("input.txt")
    part1(lines)
    part2(lines)

if __name__ == "__main__":
    main()