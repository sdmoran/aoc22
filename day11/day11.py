from enum import Enum
import math

# Read input
def read_input(fname):
    with open(fname) as f:
        lines = f.readlines()
        return [line.rstrip().strip() for line in lines]

class Mode(Enum):
    MULTIPLY = 1,
    ADD = 2,
    SQUARE = 3

class Monkey:
    def __init__(self, startingItems, operation, operationValue, testNumber, trueMonkeyNum, falseMonkeyNum):
        self.items = startingItems
        self.operation = operation
        self.operationValue = operationValue
        self.testNumber = testNumber
        self.trueMonkeyNum = trueMonkeyNum
        self.falseMonkeyNum = falseMonkeyNum
        self.inspected = 0

    # Operate on item
    # actual values don't matter... just the fact if it is divisible by the target or not. Right?
    def operate(self, item, div):
        val = 0
        if self.operation == Mode.SQUARE:
            val = item * item
        elif self.operation == Mode.MULTIPLY:
            val = item * self.operationValue
        else: # add
            val = item + self.operationValue
        self.inspected += 1

        if div:
            val = math.floor(val / 3.0)

        return val

    # test item, returning number of monkey it should be thrown to
    def test(self, item):
        if item % self.testNumber == 0:
            return self.trueMonkeyNum
        return self.falseMonkeyNum

def doRounds(monkeys, numRounds, div=True):
    # get a common factor that every value can be modded by to keep worry levels somewhat reasonable. Just product
    # of all monkey's check values will work
    modFactor = 1
    for m in monkeys:
        modFactor *= m.testNumber

    for round in range(numRounds):
        print(f"Starting round {round}")
        i = 0
        for monkey in monkeys:
            # print(f"Starting monkey {i} (test number: {monkey.testNumber}, true: {monkey.trueMonkeyNum}, false: {monkey.falseMonkeyNum})")
            for item in monkey.items:
                # perform operation
                # still needs to go to the right monkey... but doesn't need to be the full value, can just get the LCD of all monkeys' division checks :)
                item %= (modFactor)
                newValue = monkey.operate(item, div) 

                destMonkey = monkey.test(newValue)
                # Throw to next monkey
                monkeys[destMonkey].items.append(newValue)
            monkey.items = []
            i += 1

    for j in range(len(monkeys)):
        print(f"Monkey {j}: ", monkeys[j].items)
    
    sums = sorted([m.inspected for m in monkeys], reverse=True)
    print(sums)
    print(f"Total monkey business after {numRounds} rounds: : {sums[0] * sums[1]}")

def part1(monkeys):
    doRounds(monkeys, 20, div=True)

def part2(monkeys):
    doRounds(monkeys, 10000, div=False)

def main():
    lines = read_input("input.txt")

    monkeys = []

    # only 8 monkeys
    lineNum = 0
    while lineNum < len(lines):
        monkeyLines = lines[lineNum:lineNum + 6]
        print(monkeyLines)
        # line[0] is just monkey number, we can ignore
        # line[1] is starting items
        items = [int(x) for x in lines[lineNum + 1][16:].split(", ")]
        # line[2] is operation
        operationStr = lines[lineNum + 2][21:]
        if "*" in operationStr:
            # square case
            if "old" in operationStr:
                operation = Mode.SQUARE
                operationValue = 1
            # regular
            else:
                operation = Mode.MULTIPLY
                operationValue = int(operationStr[2:])
        else:
            operation = Mode.ADD
            operationValue = int(operationStr[2:])
        # line[3] is test, which is always division by some number
        testNumber = int(lines[lineNum + 3][19:])

        # line[4] is true case
        trueMonkey = int(lines[lineNum + 4][25:])
        # line[5] is false case
        falseMonkey = int(lines[lineNum + 5][25:])
        
        monkeys.append(Monkey(items, operation, operationValue, testNumber, trueMonkey, falseMonkey))

        lineNum += 7



    # part1(monkeys)
    part2(monkeys)

if __name__ == "__main__":
    main()