from enum import Enum


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


def is_hidden(
    row_idx: int, col_idx: int, tree_height: int, direction: Direction
):
    row_diff, col_diff = direction.value
    row_idx += row_diff
    col_idx += col_diff

    while (
        row_idx >= 0 and row_idx < HEIGHT and col_idx >= 0 and col_idx < WIDTH
    ):
        if TREES[row_idx][col_idx] >= tree_height:
            return True
        row_idx += row_diff
        col_idx += col_diff

    return False


visible_trees = 0

for row_idx, row in enumerate(TREES):
    for col_idx, col in enumerate(row):
        if not all(
            is_hidden(row_idx, col_idx, col, direction)
            for direction in Direction
        ):
            visible_trees += 1

print(f"{visible_trees=}")
