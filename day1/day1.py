# Read input file
def read_input(fname):
    with open(fname) as f:
        lines = f.readlines()
        return lines

# Get elf carrying most calories
def part1():
    elves = []
    lines = read_input("input.txt")
    
    cal = 0
    for line in lines:
        if len(line.rstrip()) > 1: # strip newline
            cal += int(line)
        else:
            elves.append(cal)
            cal = 0
    print(max(elves)) # most calories
    return elves

# Get top 3 elves
def part2(elves):
    elves = sorted(elves)
    print(elves[-3:]) # top 3 elves
    print(sum(elves[-3:])) # sum of top 3

def main():
    elves = part1()
    part2(elves)

if __name__ == "__main__":
    main()