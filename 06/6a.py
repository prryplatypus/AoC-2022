with open("input.txt", "r") as f:
    BUFFER = f.read()

START_CHARS_QTY = 4


def get_start(buffer: str):
    start_idx = 0
    buffer_length = len(buffer)

    while start_idx + START_CHARS_QTY <= buffer_length:
        chars = buffer[start_idx:start_idx + START_CHARS_QTY]

        if len(set(chars)) == START_CHARS_QTY:
            return start_idx + START_CHARS_QTY

        start_idx += 1


first_char_idx = get_start(BUFFER)

print(f"{first_char_idx=}")
