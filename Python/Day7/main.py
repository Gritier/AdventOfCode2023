# I need to have cards in hand ordered like "XXXXY"
# That tupled with the strength of the card
# then I should be able to sort the tuple based on strenght and cards
# sorted(tuple, key=function)
# card_map
# https://github.com/Robin270/advent_of_code/blob/master/2023/7/main.py as guide
FILE = "input.txt"
EXAMPLE = "32T3K 765\nT55J5 684\nKK677 28\nKTJJT 220\nQQQJA 483"

CARDS_VALUE_PART1 = ['2', '3', '4', '5',
                     '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
CARDS_VALUE_PART2 = ["A", "K", "Q", "T", "9",
                     "8", "7", "6", "5", "4", "3", "2", "J"]
HAND_TYPES = ["five of a kind", "four of a kind", "full house",
              "three of a kind", "two pair", "one pair", "high card"]


def read_file(file=FILE):
    with open(file, "r") as f:
        return f.read()


def parse_input(puzzle=read_file()):
    hands = []
    for line in puzzle:
        hands.append({'cards': line.split(" ")[0]})
