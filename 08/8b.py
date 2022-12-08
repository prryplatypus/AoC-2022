from enum import Enum
from functools import reduce


with open("input.txt", "r") as f:
    TREES = f.read().splitlines()
    TREES = [[int(tree) for tree in tree_row] for tree_row in TREES]
    HEIGHT = len(TREES)
    WIDTH = len(TREES[0])


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


def get_scenic_score(
    row_idx: int, col_idx: int, tree_height: int, direction: Direction
) -> int:
    score = 0

    row_diff, col_diff = direction.value
    row_idx += row_diff
    col_idx += col_diff

    while (
        row_idx >= 0 and row_idx < HEIGHT and col_idx >= 0 and col_idx < WIDTH
    ):
        score += 1
        if TREES[row_idx][col_idx] >= tree_height:
            break
        row_idx += row_diff
        col_idx += col_diff

    return score


def get_total_scenic_score(
    row_idx: int, col_idx: int, tree_height: int
) -> int:
    return reduce(
        lambda score1, score2: score1 * score2,
        (
            get_scenic_score(row_idx, col_idx, tree_height, direction)
            for direction in Direction
        ),
    )


max_scenic_score = max((
    get_total_scenic_score(row_idx, col_idx, col)
    for row_idx, row in enumerate(TREES)
    for col_idx, col in enumerate(row)
))

print(f"{max_scenic_score=}")
