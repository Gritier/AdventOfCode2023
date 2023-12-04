class Game:
    def __init__(self, gaem_id, winning_numbers, played_numbers):
        self.id = gaem_id
        self.winning_numbers = winning_numbers
        self.played_numbers = played_numbers


def read_file(file='input.txt'):
    with open(file, "r") as f:
        return f.read().splitlines()


def extract_game(line):
    game_id = int(line.split(":")[0].split(" ")[-1])
    winning_numbers = [value for value in int(
        line.split(": ")[1].split(" | ")[0].split(" "))]
    played_numbers = [value for value in int(
        line.split(": ")[1].split(" | ")[1].split(" "))]
    return Game(game_id, winning_numbers, played_numbers)


puzzle = read_file()
games = [extract_game(game) for game in puzzle]
print(games)
