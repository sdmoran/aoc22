# Read input file
def read_input(fname):
    with open(fname) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]

def part1(lines):
    # number of ranges completely contained
    total = 0
    for line in lines:
        range1, range2 = line.split(",")

        a, b = [int(x) for x in range1.split("-")]
        c, d = [int(x) for x in range2.split("-")]

        print("Checking ", range1, range2)
        # range includes another if...
        if (c >= a and d <= b):
            total += 1
        elif (a >= c and b <= d):
            total += 1

    return total

def part2(lines):
    # number of ranges overlapping
    total = 0
    for line in lines:
        range1, range2 = line.split(",")

        a, b = [int(x) for x in range1.split("-")]
        c, d = [int(x) for x in range2.split("-")]

        print("Checking ", range1, range2)
        # range overlaps if any # from a pair is between the other pairs numbers....
        if a >= c and a <= d or b >= c and b <= d:
            total += 1
        elif c >= a and c <= b or d >= a and d <= b:
            total += 1
    return total

def main():
    lines = read_input("input.txt")
    print(part1(lines))
    print(part2(lines))

if __name__ == "__main__":
    main()