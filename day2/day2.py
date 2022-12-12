# Read input file
def read_input(fname):
    with open(fname) as f:
        lines = f.readlines()
        return lines

# Common constants
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
SCORE_LOSS = 0
SCORE_DRAW = 3
SCORE_WIN = 6

moveDict = {
    # Their moves
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,

    # My moves
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS
}

scoreDict = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3
}

def part1(lines):
    score = 0
    for line in lines:
        theirMove, myMove = line.split(" ")
        score += getScoreForRound(myMove.rstrip(), theirMove)
    return score

# get score based on outcome of game, including the score for which move was chosen
def getScoreForRound(myMoveCode, theirMoveCode):
    # get translated moves
    myMove, theirMove = moveDict[myMoveCode], moveDict[theirMoveCode]
    score = 0
    # draw scenario
    if myMove == theirMove:
        score = SCORE_DRAW

    # win scenarios
    elif (myMove == ROCK and theirMove == SCISSORS) or \
        (myMove == SCISSORS and theirMove == PAPER) or \
        (myMove == PAPER and theirMove == ROCK):
        score = SCORE_WIN

    # otherwise, I lose
    else:
        score = SCORE_LOSS

    return score + scoreDict[myMove]

def part2(lines):
    score = 0
    # X: lose
    # Y: draw
    # Z: win
    for line in lines:
        # myMove determines score for outcome of round.
        # Use their move to figure out point for what symbol I choose
        theirMove, myMove = line.split(" ")
        myMove = myMove.rstrip()
        if myMove == "X":
            score += SCORE_LOSS + getMoveScoreForOutcome(theirMove, SCORE_LOSS)
        if myMove == "Y":
            score += SCORE_DRAW + getMoveScoreForOutcome(theirMove, SCORE_DRAW)
        if myMove == "Z":
            score += SCORE_WIN + getMoveScoreForOutcome(theirMove, SCORE_WIN)
    return score

# Get MY move score based on their move and the outcome
def getMoveScoreForOutcome(theirMoveCode, desiredScore):
    theirMove = moveDict[theirMoveCode]
    if desiredScore == SCORE_LOSS:
        if theirMove == ROCK:
            return scoreDict[SCISSORS]
        if theirMove == PAPER:
            return scoreDict[ROCK]
        if theirMove == SCISSORS:
            return scoreDict[PAPER]

    if desiredScore == SCORE_WIN:
        if theirMove == ROCK:
            return scoreDict[PAPER]
        if theirMove == PAPER:
            return scoreDict[SCISSORS]
        if theirMove == SCISSORS:
            return scoreDict[ROCK]
    
    return scoreDict[theirMove]
    
def main():
    lines = read_input("input.txt")
    print("Part 1: ", part1(lines))
    print("Part 2: ", part2(lines))

if __name__ == "__main__":
    main()