with open("input.txt", "r") as f:
    GROUPS = f.read().splitlines()


def get_groups():
    while GROUPS:
        elf1, elf2 = GROUPS.pop(0).split(",", 1)
        elf1_start, elf1_end = map(int, elf1.split("-"))
        elf2_start, elf2_end = map(int, elf2.split("-"))

        elf1_elements = set(range(elf1_start, elf1_end + 1))
        elf2_elements = set(range(elf2_start, elf2_end + 1))

        yield elf1_elements, elf2_elements


contained_ranges = 0

for elf1_range, elf2_range in get_groups():
    intersection = elf1_range.intersection(elf2_range)

    if intersection == elf1_range or intersection == elf2_range:
        contained_ranges += 1


print(f"{contained_ranges=}")
