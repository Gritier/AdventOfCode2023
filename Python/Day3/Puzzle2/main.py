# Got helped by gentlemens on the Advent Of Code subreddit!
import re
from collections import defaultdict
from math import prod


def read_input(file='input.txt'):
    puzzle = []
    with open(file, 'r') as f:
        puzzle = f.read().splitlines()
    return puzzle


def symbols_coordinates(puzzle):
    symbols = dict()
    for y, line in enumerate(puzzle):
        for x, c in enumerate(line):
            if c not in "1234567890.":
                symbols[(x, y)] = c
    return symbols


def solve(puzzle=read_input()):
    symbols = symbols_coordinates(puzzle)
    gears = defaultdict(list)
    part_numbers_sum = 0
    for y, line in enumerate(puzzle):
        for match in re.finditer(r"\d+", line):
            for (s_x, s_y), c in symbols.items():
                if (match.start() - 1 <= s_x <= match.end()) and (y - 1 <= s_y <= y + 1):
                    num = int(match.group())
                    part_numbers_sum += num
                    if c == "*":
                        gears[(s_x, s_y)].append(num)
                    break
    gear_ratios = sum(prod(part_nums)
                      for part_nums in gears.values() if len(part_nums) == 2)
    return [part_numbers_sum, gear_ratios]


print(solve()[1])
