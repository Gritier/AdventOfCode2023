class Game:
    def __init__(self, id, sets):
        self.id = id
        self.sets = sets

    def get_id(self):
        return self.id

    def get_sets(self):
        return self.sets

    def __str__(self):
        return f'ID: {self.id}\nSets: {self.sets}'

    def analyze_sets(self):
        max_values = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        for set in self.sets:
            for extraction in set.split(', '):
                value, key = int(extraction.split(
                    " ")[0]), extraction.split(" ")[1]
                if value > max_values[key]:
                    max_values[key] = value

        return [max_values]


rules = {
    'red': 12,
    'green': 13,
    'blue': 14
}

input = []
games = []
result = [0, 0]


def check(max_set):
    for key in max_set:
        if max_set[key] > rules[key]:
            return False
    return True


with open("input.txt", "r") as puzzle:
    input = puzzle.read().splitlines()

for line in input:
    game_sets = []
    game_id = int(line.split(":")[0].split(' ')[1])
    for set in line.split(": ")[1].split("; "):
        game_sets.append(set)
    games.append(Game(game_id, game_sets))

for game in games:
    max_values = game.analyze_sets()[0]
    if check(max_values):
        result[0] += game.get_id()
    result[1] += max_values['red']*max_values['green']*max_values['blue']

print(result[0])
print(result[1])
