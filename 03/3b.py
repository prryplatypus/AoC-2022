with open("input.txt", "r") as f:
    RUCKSACKS = f.read().splitlines()

LETTERS = "abcdefghijklmnopqrstuvwxyz"
PRIORITIES = {
    **{letter: index + 1 for index, letter in enumerate(LETTERS)},
    **{letter.upper(): index + 26 + 1 for index, letter in enumerate(LETTERS)},
}


def get_groups():
    while RUCKSACKS:
        yield (
            set(RUCKSACKS.pop(0)),
            RUCKSACKS.pop(0),
            RUCKSACKS.pop(0),
        )


priorities_sum = 0

for elf1, elf2, elf3 in get_groups():
    common_item, = elf1.intersection(elf2, elf3)
    priorities_sum += PRIORITIES[common_item]

print(f"{priorities_sum=}")
