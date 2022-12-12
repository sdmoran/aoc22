# Read input file
def read_input(fname):
    with open(fname) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]

def getPriority(letter):
    # use 64 as offset for A-Z
    if 65 <= ord(letter) and ord(letter) <= 96:
        return ord(letter) - 38 # normalize "A" to 1
    # use 96 as offset for a-z
    else:
        return ord(letter) - 96 # normalize "a" to 1

def part1(lines):
    # sum of all matching priorities
    score = 0

    for line in lines:
        length = int(len(line) / 2)
        half1 = line[0:length]
        half2 = line[length:]
        half1set = set()
        half2set = set()

        # given that len(half1) == len(half2) so no need to be careful about range here
        for i in range(length):
            half1set.add(half1[i])
            half2set.add(half2[i])
            combo = half1set.intersection(half2set)
            if len(combo) > 0:
                score += getPriority(combo.pop())
                break

    return score

LINES_IN_GROUP = 3

# so, same thing but with 3 inputs... of different sizes.
def part2(lines):
    score = 0

    # assume input valid; evenly divisible int groups of 3
    for i in range(int(len(lines) / LINES_IN_GROUP)):
        bags = []
        for _ in range(LINES_IN_GROUP):
            bags.append(set())
            
        for j in range(LINES_IN_GROUP):
            for letter in lines[i * LINES_IN_GROUP + j]:
                bags[j].add(letter)
    
        combo = None
        for k in range(LINES_IN_GROUP):
            if combo == None:
                a = bags[k]
                b = bags[k + 1]
                combo = a.intersection(b)
            else:
                combo = combo.intersection(bags[k])

        score += getPriority(combo.pop())

    return score

    





def main():
    lines = read_input("input.txt")
    print(part1(lines))
    print(part2(lines))

if __name__ == "__main__":
    main()