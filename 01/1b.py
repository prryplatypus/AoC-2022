with open("input.txt") as f:
    lines = f.readlines()


all_elf_cals = []
curr_elf, curr_cal = 1, 0

for line in lines:
    stripped = line.strip()
    if stripped == "":
        all_elf_cals.append((curr_cal, curr_elf))
        curr_elf += 1
        curr_cal = 0
        continue

    curr_cal += int(stripped)

all_elf_cals.sort()

highest_3_cals = all_elf_cals[-3:]
highest_3_cals_sum = sum([x[0] for x in highest_3_cals])

print(f"{highest_3_cals=}")
print(f"{highest_3_cals_sum=}")
