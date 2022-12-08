from __future__ import annotations

from functools import cache
from typing import Dict, List, Optional, Tuple


with open("input.txt", "r") as f:
    STDIO = f.read().splitlines()

TOTAL_SPACE = 70_000_000
NEEDED_UNUSED_SPACE = 30_000_000


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name: str, parent: Optional[Directory] = None):
        self.name = name
        self.parent = parent
        self.children: Dict[str, Directory] = {}
        self.files: List[File] = []

    def get_or_create_child(self, name: str) -> Directory:
        if name not in self.children:
            self.children[name] = Directory(name, self)
        return self.children[name]

    def cd(self, path: str) -> Directory:
        if path == "..":
            return self.parent or self

        if path == "/":
            current = self
            parent = current.parent

            while parent is not None:
                current = parent
                parent = current.parent

            return current

        return self.get_or_create_child(path)

    @property
    @cache
    def size(self) -> int:
        files_sum = sum(file.size for file in self.files)
        children_sum = sum(child.size for child in self.children.values())
        return files_sum + children_sum


def get_dirs_with_minimum_size_limit(
    root: Directory, limit: int
) -> List[Directory]:
    dirs = []

    for dir in root.children.values():
        if dir.size >= limit:
            dirs.append(dir)
        dirs.extend(get_dirs_with_minimum_size_limit(dir, limit))

    return dirs


def parse_command(line: str) -> Tuple[str, Optional[str]]:
    cmd = line[2:]
    if cmd.startswith("cd"):
        return tuple(cmd.split(" ", 1))
    return cmd, None  # Parse ls


def parse_ls(curr_dir: Directory) -> None:
    while STDIO and not STDIO[0].startswith("$ "):
        line = STDIO.pop(0)
        misc, name = line.split(" ", 1)

        if misc == "dir":
            curr_dir.get_or_create_child(name)
            continue

        curr_dir.files.append(File(name, int(misc)))


root = Directory("/")
curr_dir = root


while STDIO:
    line = STDIO.pop(0)
    cmd, args = parse_command(line)

    if cmd == "cd":
        assert args is not None
        curr_dir = curr_dir.cd(args)
    elif cmd == "ls":
        parse_ls(curr_dir)


space_available = TOTAL_SPACE - root.size
space_to_free = NEEDED_UNUSED_SPACE - space_available

candidates_to_delete = get_dirs_with_minimum_size_limit(root, space_to_free)
best_candidate = min(candidates_to_delete, key=lambda dir: dir.size)

print(f"{best_candidate.size=}")
