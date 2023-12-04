import re
class Game:
    def __init__(self, game_id, winning_numbers, played_numbers):
        self.game_id = game_id
        self.winning_numbers = winning_numbers
        self.played_numbers = played_numbers

    def __str__(self):
        return f'Game ID: {self.game_id}\nGame ID: {self.winning_numbers}\nGame ID: {self.played_numbers}\n'

def read_file(file='input.txt'):
    with open(file, "r") as f:
        return f.read().splitlines()


def extract_game(line):
    game_id = int(line.split(":")[0].split(" ")[-1])
    winning_numbers =  [value.group() for value in re.finditer(r"\d+",
        line.split(": ")[1].split(" | ")[0])]
    played_numbers = [value.group() for value in re.finditer(r"\d+",
        line.split(": ")[1].split(" | ")[1])]
    return Game(game_id, winning_numbers, played_numbers)

def get_wins(game):
    wins = 0
    for played in game.played_numbers:
        if played in game.winning_numbers:
            wins += 1
    return wins

puzzle = read_file()
games = [extract_game(game) for game in puzzle]
total_cards = games

for card in total_cards:
    for i in range(card.game_id, card.game_id+get_wins(card)):
        if games[i]:
            total_cards.append(games[i])

print(len(total_cards))


