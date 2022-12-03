with open("input.txt", "r") as f:
    RUCKSACKS = f.read().splitlines()

LETTERS = "abcdefghijklmnopqrstuvwxyz"
PRIORITIES = {
    **{letter: index + 1 for index, letter in enumerate(LETTERS)},
    **{letter.upper(): index + 26 + 1 for index, letter in enumerate(LETTERS)},
}


def get_rucksacks():
    while RUCKSACKS:
        yield RUCKSACKS.pop(0)


priorities_sum = 0

for rucksack in get_rucksacks():
    items_per_pocket = len(rucksack) // 2
    first_pocket, second_pocket = (
        set(rucksack[:items_per_pocket]), set(rucksack[items_per_pocket:])
    )
    shared_item, = first_pocket.intersection(second_pocket)
    priorities_sum += PRIORITIES[shared_item]

print(f"{priorities_sum=}")
