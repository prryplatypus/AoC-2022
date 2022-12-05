with open("input.txt", "r") as f:
    FILE = f.read()
    STACK_STR, INSTRUCTIONS_STR = FILE.split("\n\n", 1)
    STACK, INSTRUCTIONS = STACK_STR.splitlines(), INSTRUCTIONS_STR.splitlines()


def get_stacks():
    stacks = []

    STACK.pop()  # Remove the stack numbers
    while STACK:
        line = STACK.pop(0)
        line_elements = []

        while line:
            value = line[:3].strip(" []")
            line_elements.append(value)
            line = line[4:]

        if not stacks:
            stacks = [[] for _ in range(len(line_elements))]

        for i, value in enumerate(line_elements):
            if value:
                stacks[i].append(value)

    for stack in stacks:
        stack.reverse()

    return stacks


def do_move(stacks, from_, to, qty):
    vals = stacks[from_ - 1][-qty:]
    stacks[from_ - 1] = stacks[from_ - 1][:-qty]
    stacks[to - 1].extend(vals)


stacks = get_stacks()
for instruction in INSTRUCTIONS:
    _, qty, _, from_, _, to = instruction.split()
    do_move(stacks, int(from_), int(to), int(qty))


for stack in stacks:
    print(stack[-1], end='')
