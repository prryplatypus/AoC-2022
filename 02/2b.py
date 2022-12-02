with open("input.txt", "r") as f:
    LINES = f.read().splitlines()

LOST, DRAW, WON = 0, 3, 6
DO_LOSE, DO_DRAW, DO_WIN = "X", "Y", "Z"
ROCK, PAPER, SCISSORS = "A", "B", "C"

WIN_CHOICES = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK,
}
LOSE_CHOICES = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER,
}
PLAY_VALUES = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}


total_score = 0

for line in LINES:
    oponent, player = line.split(" ")

    if player == DO_LOSE:
        player_value = LOSE_CHOICES[oponent]
        total_score += LOST
        total_score += PLAY_VALUES[player_value]
        continue

    if player == DO_DRAW:
        player_value = oponent
        total_score += DRAW
        total_score += PLAY_VALUES[player_value]
        continue

    if player == DO_WIN:
        player_value = WIN_CHOICES[oponent]
        total_score += WON
        total_score += PLAY_VALUES[player_value]

print(f"{total_score=}")
