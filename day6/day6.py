# Read input
def read_input(fname):
    with open(fname) as f:
        lines = f.readlines()
        return [line.rstrip() for line in lines]

def part1(line):
    arr = list(line[:4])
    print(arr)

    i = 4
    while i< len(line):
        c = line[i]
        arr.pop(0)
        arr.append(c)
    
        if len(set(arr)) == 4:
            return i + 1
        i += 1

def part2(line):
    arr = list(line[:14])
    print(arr)

    i = 14
    while i< len(line):
        c = line[i]
        arr.pop(0)
        arr.append(c)
    
        if len(set(arr)) == 14:
            return i + 1
        i += 1
    

def main():
    lines = read_input("input.txt")
    result = part1(lines[0])
    print(result)
    result = part2(lines[0])
    print(result)




if __name__ == "__main__":
    main()