with open("input.txt", "r") as f:
    LINES = f.read().splitlines()

LOST, DRAW, WON = 0, 3, 6
ROCK, PAPER, SCISSORS = "X", "Y", "Z"

PLAY_VALUES = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}
EQUIVALENT_MOVES = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
}
DEFEAT_MAP = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER,
}


total_score = 0

for line in LINES:
    oponent, player = line.split(" ")
    oponent = EQUIVALENT_MOVES[oponent]

    total_score += PLAY_VALUES[player]

    if oponent == player:
        total_score += DRAW
        continue

    if DEFEAT_MAP[oponent] == player:
        total_score += LOST
        continue

    if DEFEAT_MAP[player] == oponent:
        total_score += WON

print(f"{total_score=}")
