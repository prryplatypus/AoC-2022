with open("input.txt") as f:
    lines = f.readlines()

max_elf, max_cal = None, 0
curr_elf, curr_cal = 1, 0

for line in lines:
    stripped = line.strip()
    if stripped == "":
        if curr_cal > max_cal:
            max_cal = curr_cal
            max_elf = curr_elf

        curr_elf += 1
        curr_cal = 0
        continue

    curr_cal += int(stripped)

print(f"Elf {max_elf} has the most calories: {max_cal}")
